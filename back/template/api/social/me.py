import datetime

from flask import jsonify
from flask_jwt_extended import get_jwt_identity

from template.auth import authenticated
from template.managers.social import users


@authenticated
def me():
    me_id = get_jwt_identity()['id']
    user = users.get(me_id)
    user.last_login = datetime.datetime.now()
    user.save()
    me = user.get_data()
    return jsonify(me)
