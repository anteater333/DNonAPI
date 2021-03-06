from flask import request
from flask_restx import Resource

from ..util.decorator import token_required, prove_yourself
from ..util.dto import UserDto, SavedInfoDto
from ..service.user_service import save_new_user, get_all_users, get_a_user, delete_a_user
from ..service.saved_service import load_user_game_progress

import re

api = UserDto.api
_user = UserDto.user
_saved_info = SavedInfoDto.saved_info

@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user)
    def get(self):
        """List all registred users"""
        return get_all_users()

    @api.response(201, 'User successfully created.')
    @api.response(409, 'User already exists.')
    @api.response(422, 'Invalid username.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User"""
        data = request.json
        # Checking name validation
        if not re.match("^[\w\d_-]*$", data['userName']):
            api.abort(422, 'The name can only have letters, numbers, underscores and dashes.')

        return save_new_user(data=data)


@api.route('/<userName>')
@api.param('userName', 'The User name')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_list_with(_user)   # user를 dto에 맞춰 serializable 하게 변환
    def get(self, userName):
        """Get a user given their name"""
        user = get_a_user(userName)
        if not user:
            api.abort(404)
        else:
            return user

    @prove_yourself
    @api.marshal_with(_user)
    @api.doc('unsubscribe this user')
    def delete(self, userName):
        """Delete user from server"""
        user = delete_a_user(userName)
        if not user:
            api.abort(404)
        else:
            return user

@api.route('/<userName>/saved-info/<savedId>')
@api.param('userName', 'User name who owns data')
@api.param('savedId', 'Unique saved data identifier')
@api.response(404, 'Data not found.')
class SavedInfo(Resource):
    @prove_yourself
    @api.doc('get and delete a saved game progress.')
    @api.marshal_with(_saved_info)
    def delete(self, userName, savedId):
        """Get and delete a signed user's saved data."""
        saved_data = load_user_game_progress(savedId, userName)
        if not saved_data:
            api.abort(404, 'data not found')
        return saved_data