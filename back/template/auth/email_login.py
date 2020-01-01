import hashlib
from datetime import datetime

from flask import Blueprint, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity
from itsdangerous import URLSafeTimedSerializer
from peewee import DoesNotExist

from template.core import config, db, cache, queue, mail
from template.exceptions import *
from template.models.social import User
from .utils import authenticated


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
        except DoesNotExist:
            raise UserNotFound

        if password is None:
            raise PasswordRequired
        password = hashlib.sha3_256('{}-{}'.format(config['email_auth']['hash_key'], password).encode())
        if user.password != password.hexdigest():
            raise EmailPasswordMismatch

        user.last_login = datetime.now()
        user.first_login = False
        user.save()
        access_token = create_access_token(identity=user.get_identity())

        return jsonify(access_token=access_token), 200

    @email_auth_bp.route('/sign-up', methods=['POST'])
    @db.connection_context()
    def sign_up():
        email = request.json.get('email')
        password = request.json.get('password')
        first_name = request.json.get('first_name')
        last_name = request.json.get('last_name')

        try:
            User.get(email=email)
            raise EmailAddressAlreadyTaken
        except DoesNotExist:
            if password is None:
                raise PasswordRequired
            if len(password) < 8:
                raise PasswordTooShort
            if email is None:
                raise EmailRequired
            if first_name is None:
                raise FirstNameRequired
            if last_name is None:
                raise LastNameRequired

            hashed_password = hashlib.sha3_256('{}-{}'.format(config['email_auth']['hash_key'], password).encode())

            user = User.create(email=email, password=hashed_password.hexdigest(), last_login=datetime.now(),
                               first_login=True, created_at=datetime.now(), first_name=first_name, last_name=last_name)

            activation_token = generate_activation_token(email)
            queue.enqueue(send_activation_email, user.email, activation_token)

            access_token = create_access_token(identity=user.get_identity())

            return jsonify(access_token=access_token), 200

    @email_auth_bp.route('/check-token/<activation_token>')
    @db.connection_context()
    def check_token(activation_token):
        email = check_activation_token(activation_token)
        try:
            user = User.get(email=email)
        except DoesNotExist:
            raise UserNotFound

        if user.account_activated:
            raise InvalidConfirmationLink

        return jsonify(email=email)

    @email_auth_bp.route('/confirm-email/<activation_token>', methods=['POST'])
    @db.connection_context()
    @authenticated
    def confirm_email(activation_token):
        email = check_activation_token(activation_token)
        original_email = get_jwt_identity()['email']
        if original_email != email:
            raise InvalidConfirmationLink

        try:
            user = User.get(email=email)
        except DoesNotExist:
            raise UserNotFound

        if user.account_activated:
            raise InvalidConfirmationLink
        else:
            user.account_activated = True
            user.confirmation_date = datetime.now()
            user.save()

            return 'Your account has been activated successfully!', 200

    @email_auth_bp.route('/resend-email', methods=['POST'])
    @db.connection_context()
    @authenticated
    def resend_email():
        email = get_jwt_identity()['email']

        try:
            user = User.get(email=email)
        except DoesNotExist:
            raise UserNotFound

        if user.google_auth or user.account_activated:
            raise AccountAlreadyActivated

        activation_token = generate_activation_token(email)
        queue.enqueue(send_activation_email, email, activation_token)

        return 'A new email has been sent to {}'.format(email), 200

    app.register_blueprint(email_auth_bp, url_prefix="/auth/email")


def generate_activation_token(email):
    serializer = URLSafeTimedSerializer(config['email_auth']['activation_key'])
    return serializer.dumps(email, salt=config['email_auth']['activation_password'])


def send_activation_email(to, activation_token):
    mail.no_reply.connect()
    mail.no_reply.sendmail(to, 'Confirm your email address', 'confirm_email',
                           confirmation_url='{}/login/{}'.format(config['front_root_url'], activation_token))
    mail.no_reply.close()


def check_activation_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(config['email_auth']['activation_key'])
    try:
        email = serializer.loads(
            token,
            salt=config['email_auth']['activation_password'],
            max_age=expiration
        )
    except:
        raise InvalidConfirmationLink

    return email
