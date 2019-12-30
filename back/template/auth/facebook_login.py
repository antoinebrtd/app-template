from datetime import datetime

import requests
from flask import Blueprint, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token

from template.core import cache
from template.exceptions.users import *
from template.models.social import User

FACEBOOK_ME_URL = 'https://graph.facebook.com/me?fields=first_name,last_name,email&access_token={}'
FACEBOOK_PICTURE_URL = 'https://graph.facebook.com/{}/picture'


def create_facebook_auth(app):
    jwt = JWTManager(app)
    facebook_auth_bp = Blueprint('facebook_login', __name__)

    def credentials_to_dict(credentials):
        return {'token': credentials['accessToken'],
                'fb_user_id': credentials['userID'],
                'expires_in': credentials['expiresIn'],
                'signed_request': credentials['signedRequest'],
                'data_access_expiration_time': credentials['data_access_expiration_time']}

    @facebook_auth_bp.errorhandler(UserError)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    @facebook_auth_bp.route('/login', methods=['POST'])
    def login():
        credentials = credentials_to_dict(request.json)
        response = requests.get(FACEBOOK_ME_URL.format(credentials['token']))
        if response.status_code != 200:
            raise FacebookLoginError
        user_info = response.json()
        email = user_info.get('email')
        user, created = User.get_or_create(email=email, defaults={
            'first_name': user_info.get('first_name'),
            'last_name': user_info.get('last_name'),
            'picture': FACEBOOK_PICTURE_URL.format(credentials['fb_user_id']),
            'last_login': datetime.now(),
            'facebook_auth': True,
            'user_confirmed': True
        })

        user.add_facebook_credentials(credentials)

        access_token = create_access_token(identity=user.get_identity())

        return jsonify(access_token=access_token), 200

    @jwt.token_in_blacklist_loader
    def check_if_token_is_revoked(decrypted_token):
        user_id = decrypted_token['identity']['id']
        entry = cache.get('user_{}_valid'.format(user_id))
        if entry is None:
            return False
        return entry == 'false'

    app.register_blueprint(facebook_auth_bp, url_prefix="/auth/facebook")
