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
        'playerId': fields.Integer(readonly=True, required=False),
        'playerName': fields.String(description='Player\'s name'),
        'guest': fields.Boolean(readonly=True, required=False, description='Guest user or not'),
        'highscore': fields.Integer(readonly=True, required=False, description='Highest point player scored'),
        'dateEntered': fields.DateTime(readonly=True, required=False, description='Date player entered this channel')
    })

    channel = api.model(name='ch', model={
        'channelId': fields.Integer(readonly=True, description='Unique channel identifier'),
        'battlefieldId': fields.Integer(description='Unique battlefield identifier'),
        'battlefield': fields.Nested(model=battlefield, readonly=True, description='Channel\'s battlefield'),
        'maximum': fields.Integer(description='Maximum participants number'),
        'ranking': fields.List(fields.Nested(model=player), readonly=True, description='Player ranking for this channel'),        
        'participants': fields.List(fields.Nested(model=player), readonly=True, description='Players now participating this game')
    })

class SavedInfoDto:
    api = Namespace('saved-info', description='Operations for saving in-game data')

    location = api.model(name='location', model={
        'x': fields.Integer(),
        'y': fields.Integer()
    })

    saving_info = api.model(name='saving-info', model={
        'channelId': fields.Integer(description='Identifier for channel that game belongs'),
        'playerName': fields.String(description='The player\'s name'),
        'score': fields.Integer(description='The point that player gained till saves the game info'),
        'location': fields.Nested(model=location, description='The location player saved this data and quit the gmae.'),
        'items': fields.List(fields.String(), description='List of items the player has')
    })

    saved_info = api.model(name='saved-info', model={
        'guest': fields.Boolean(required=False, readonly=True, description='Whether this player is guest or signed'),
        'savedId': fields.Integer(required=False, readonly=True, description='Unique saved-info identifier'),
        'guestPassword': fields.String(required=False, readonly=True, description='One-time password needed when loading the info'),
        'channelId': fields.Integer(description='Identifier for channel that game belongs'),
        'playerName': fields.String(description='The player\'s name'),
        'score': fields.Integer(description='The point that player gained till saves the game info'),
        'location': fields.Nested(model=location, description='The location player saved this data and quit the gmae.'),
        'items': fields.List(fields.String(), description='List of items the player has'),
        'dateSaved': fields.DateTime(required=False, readonly=True, description='The date player saved this game')
    })