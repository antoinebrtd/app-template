import google_auth_oauthlib.flow
import googleapiclient.discovery

from datetime import datetime
from flask import Blueprint, jsonify, request, redirect
from flask_jwt_extended import JWTManager, create_access_token

from template.core import config, db, cache
from template.exceptions.users import *
from template.models.social import User

SCOPES = ['https://www.googleapis.com/auth/userinfo.profile',
          'https://www.googleapis.com/auth/userinfo.email', 'openid']


def create_google_auth(app):
    jwt = JWTManager(app)
    google_auth_bp = Blueprint('login', __name__)

    def credentials_to_dict(credentials):
        return {'token': credentials.token,
                'refresh_token': credentials.refresh_token,
                'token_uri': credentials.token_uri,
                'client_id': credentials.client_id,
                'client_secret': credentials.client_secret,
                'scopes': credentials.scopes}

    @google_auth_bp.errorhandler(UsersError)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    @google_auth_bp.route('/callback')
    def callback():
        code = request.args.get('code')
        state = request.args.get('state')
        return redirect('{}?code={}&state={}'.format(config['oauth']['front_callback'], code, state))

    @google_auth_bp.route('/login')
    def login():
        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(config['oauth']['google_config'], scopes=SCOPES)
        flow.redirect_uri = config['oauth']['callback']
        authorization_url, state = flow.authorization_url(
            access_type='offline',
            prompt='consent')
        return jsonify({'url': authorization_url})

    @google_auth_bp.route('/authorize')
    @db.connection_context()
    def authorize():
        code = request.args.get('code')
        state = request.args.get('state')
        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(config['oauth']['google_config'], scopes=SCOPES,
                                                                       state=state)
        flow.redirect_uri = config['oauth']['callback']
        flow.fetch_token(code=code)

        credentials = flow.credentials

        user_info_service = googleapiclient.discovery.build("oauth2", "v2", credentials=credentials,
                                                            cache_discovery=False)

        user_info = user_info_service.userinfo().get().execute()
        email = user_info.get('email')
        user, created = User.get_or_create(email=email, defaults={
            'first_name': user_info.get('given_name'),
            'last_name': user_info.get('family_name'),
            'picture': user_info.get('picture'),
            'last_login': datetime.now(),
        })

        user.add_credentials(credentials_to_dict(credentials))

        access_token = create_access_token(identity=user.get_identity())

        return jsonify(access_token=access_token), 200

    @jwt.token_in_blacklist_loader
    def check_if_token_is_revoked(decrypted_token):
        user_id = decrypted_token['identity']['id']
        entry = cache.get('user_{}_valid'.format(user_id))
        if entry is None:
            return False
        return entry == 'false'

    app.register_blueprint(google_auth_bp, url_prefix="/google/auth")
