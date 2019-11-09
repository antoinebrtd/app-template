import hashlib
from datetime import datetime

from flask import Blueprint, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token
from peewee import DoesNotExist

from template.core import config, db, cache
from template.exceptions import *
from template.models.social import User


def create_email_auth(app):
    jwt = JWTManager(app)
    email_auth_bp = Blueprint('email_login', __name__)

    @jwt.token_in_blacklist_loader
    def check_if_token_is_revoked(decrypted_token):
        user_id = decrypted_token['identity']['id']
        entry = cache.get('user_{}_valid'.format(user_id))
        if entry is None:
            return False
        return entry == 'false'

    @email_auth_bp.errorhandler(UserError)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    @email_auth_bp.errorhandler(PasswordError)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    @email_auth_bp.route('/login', methods=['POST'])
    @db.connection_context()
    def login():
        email = request.json.get('email')
        password = request.json.get('password')

        try:
            user = User.get(email=email)
            if not user.email_auth:
                raise LoginWithGoogle
        except DoesNotExist:
            raise UserNotFound

        if password is None:
            raise PasswordRequired
        password = hashlib.sha3_256('{}-{}'.format(config['email_auth']['hash_key'], password).encode())
        if user.password != password.hexdigest():
            raise EmailPasswordMismatch

        user.last_login = datetime.now()
        user.save()
        access_token = create_access_token(identity=user.get_identity())

        return jsonify(access_token=access_token), 200

    @email_auth_bp.route('/sign-up', methods=['POST'])
    @db.connection_context()
    def sign_up():
        email = request.json.get('email')
        password = request.json.get('password')

        try:
            User.get(email=email)
            raise EmailAddressAlreadyTaken
        except DoesNotExist:
            if password is None:
                raise PasswordRequired
            if len(password) < 8:
                raise PasswordTooShort

            hashed_password = hashlib.sha3_256('{}-{}'.format(config['email_auth']['hash_key'], password).encode())

            user = User.create(email=email, password=hashed_password.hexdigest(), last_login=datetime.now(),
                               email_auth=True)

            access_token = create_access_token(identity=user.get_identity())

            return jsonify(access_token=access_token), 200

    app.register_blueprint(email_auth_bp, url_prefix="/email/auth")
