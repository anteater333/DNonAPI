from flask import request
from flask_restx import Resource

from ..util.decorator import token_required, admin_token_required
from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user

api = UserDto.api
_user = UserDto.user

@api.route('/')
class UserList(Resource):
    @token_required
    @api.doc('list_of_registred_users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registred users"""
        return get_all_users()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User"""
        data = request.json
        return save_new_user(data=data)


@api.route('/<userName>')
@api.param('userName', 'The User name')
@api.response(404, 'User not found.')
class User(Resource):
    @admin_token_required
    @api.doc('get a user')
    @api.marshal_list_with(_user)
    def get(self, userName):
        """get a user given their name"""
        user = get_a_user(userName)
        if not user:
            api.abort(404)
        else:
            return user