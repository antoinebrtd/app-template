from template.api import api_bp, api

from .me import me
from .users import User, Users

api_bp.add_url_rule('/me', 'me', me)
api.add_resource(Users, '/users')
api.add_resource(User, '/users/<user_id>')
