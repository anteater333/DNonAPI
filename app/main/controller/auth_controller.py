from flask import request
from flask_restx import Resource

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth

@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.response(200, 'user successfully logged in.')
    @api.response(401, 'Wrong auth info.')
    @api.expect(user_auth, validate=True)
    def post(self):
        """Login and get a token for auth"""
        # get the post data
        post_data = request.json
        return Auth.login_user(data=post_data)

@api.route('/logout')
class LogoutAPI(Resource):
    """
        Logout Resource
    """
    @api.doc('logout a user')
    @api.response(403, 'Invalid auth token.')
    def post(self):
        """Logout and destroy current token"""
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)