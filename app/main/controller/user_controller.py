from flask import request
from flask_restx import Resource

from ..util.decorator import token_required, prove_yourself
from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user, delete_a_user

api = UserDto.api
_user = UserDto.user

@api.route('/')
class UserList(Resource):
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
    @api.doc('get a user')
    @api.marshal_list_with(_user)   # user를 dto에 맞춰 serializable 하게 변환
    def get(self, userName):
        """get a user given their name"""
        user = get_a_user(userName)
        if not user:
            api.abort(404)
        else:
            return user

    @prove_yourself
    @api.marshal_with(_user)
    @api.doc('unsubscribe this user')
    def delete(self, userName):
        """delete user from database"""
        user = delete_a_user(userName)
        if not user:
            api.abort(404)
        else:
            return user