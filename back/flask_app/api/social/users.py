from flask import request
from flask_jwt_extended import get_jwt_identity
from flask_restful import Resource

from flask_app.auth import authenticated
from flask_app.managers.social import users


class Users(Resource):
    @authenticated
    def get(self):
        search = request.args.get('search', None)
        user_list = users.get_all(search=search)
        return {'msg': 'success', 'users': user_list}

    @authenticated
    def put(self):
        email = request.json['email']
        team = request.json['team']
        user = users.add_user(email, team)
        return {'msg': 'success', 'user': user}


class User(Resource):
    @authenticated
    def get(self, user_id):
        identity = get_jwt_identity()
        user = users.get(identity['id'])
        if identity['id'] != user_id and not user.admin:
            return {'msg': 'forbidden'}, 403
        return {'msg': 'success', 'user': users.get(user_id).get_data()}

    @authenticated
    def delete(self, user_id):
        users.delete_user(user_id)
        return {'msg': 'success'}
