from flask import jsonify
from flask_jwt_extended import get_jwt_identity

from template.auth import authenticated
from template.managers.social import users


@authenticated
def me():
    me_id = get_jwt_identity()['id']
    user = users.get(me_id)
    profile, account_activated, auth_type, first_login = user.get_data()
    return jsonify({'profile': profile, 'account_activated': account_activated, 'auth_type': auth_type,
                    'first_login': first_login})
