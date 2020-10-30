from flask_restx import Namespace, fields

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model(name='user', model={
        'userId': fields.Integer(readonly=True, description='Unique user identifier'),
        'userName': fields.String(required=True, description='user name'),
        'email': fields.String(required=True, description='user email address'),
        'userPassword': fields.String(required=True, description="user password"),
        'dateRegistered': fields.DateTime(readonly=True, description="date user registered")
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model(name='auth_details', model={
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password')
    })

class ChannelDto:
    api = Namespace('ch', description='channel related operations')
    channel = api.model(name='ch', model={
        'id': fields.Integer(readonly=True, description='Unique channel identifier'),
        'ranking': fields.List(fields.String(), readonly=True, description='Player ranking for this channel'),
        'maximum': fields.Integer(description='Maximum participants number')
    })