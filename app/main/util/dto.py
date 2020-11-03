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

# class BattlefieldDto:
#     api = Namespace('bf', description='Battlefield info')

#     battlefield = api.model(name='bf', model={
#         'battlefieldId': fields.Integer(readonly=True, description='Unique identifier'),
#         'battlefieldName': fields.String(description='The battlefield\'s name'),
#         'description': fields.String(description=''),
#         'geography': fields.List(fields.List(fields.Integer()), description='The map')
#     })

class ChannelDto:
    api = Namespace('ch', description='channel related operations')

    battlefield = api.model(name='bf', model={
        'battlefieldId': fields.Integer(readonly=True, description='Unique identifier'),
        'battlefieldName': fields.String(description='The battlefield\'s name'),
        'description': fields.String(description=''),
        'geography': fields.List(fields.List(fields.Integer()), description='The map')
    })

    player = api.model(name='player', model={
        'playerName': fields.String(),
        'signed': fields.Boolean(readonly=True),
        'highscore': fields.Integer(readonly=True)
    })

    channel = api.model(name='ch', model={
        'channelId': fields.Integer(readonly=True, description='Unique channel identifier'),
        'battlefieldId': fields.Integer(description='Unique battlefield identifier'),
        'battlefield': fields.Nested(model=battlefield, readonly=True, description='Channel\'s battlefield'),
        'maximum': fields.Integer(description='Maximum participants number'),
        'ranking': fields.List(fields.Nested(model=player), readonly=True, description='Player ranking for this channel'),        
        'participants': fields.List(fields.Nested(model=player), readonly=True, description='Players now participating this game')
    })

class SaveDto:
    api = Namesapce('save', description='Operations for saving in-game data')

    save_info = api.model(name='save-info', model={
        
    })