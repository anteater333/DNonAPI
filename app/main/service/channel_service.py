import datetime

from app.main.model.channel import Channel, PlayerInfo
from app.main.model.battlefield import Battlefield
from app.main.model.counter import Counter

from pymodm.errors import DoesNotExist, ValidationError
from pymongo.errors import DuplicateKeyError

def given_max_is_valid(max):
    return 8 <= max and max <= 32

def save_new_channel(data):
    if not given_max_is_valid(data['maximum']):
        response_object = {
            'status': 'fail',
            'message': 'The maximum number of players should be at least 8 and less than 32.'
        }
        return response_object, 409

    try:
        battlefield = Battlefield.objects.get({'_id': data['battlefieldId']})
        
        new_channel = Channel(
            channelId=Counter.getNextSequence('channelId'),
            maximum=data['maximum'],
            battlefield=battlefield
        )
        
        new_channel.save()
    except DoesNotExist:
        response_object = {
            'status': 'fail',
            'message': 'No such map'
        }
        return response_object, 404
    except DuplicateKeyError:
        response_object = {
            'status': 'fail',
            'message': 'Duplicated key error.'
        }
        return response_object, 409
    else:
        response_object = {
            'status': 'success',
            'message': 'A new channel has successfully been added.'
        }
        return response_object, 201

def get_all_channels():
    return list(Channel.objects.all())

def get_a_channel(channelId):
    try:
        return Channel.objects.get({'_id': int(channelId)})
    except DoesNotExist:
        return None

def update_a_channel(channelId, data):
    if not given_max_is_valid(data['maximum']):
        response_object = {
            'status': 'fail',
            'message': 'The maximum number of players should be at least 8 and less than 32.'
        }
        return response_object, 409
    try:
        channel = Channel.objects.get({'_id': int(channelId)})

        if data['maximum']:
            channel.maximum = data['maximum']
        
        if data['battlefieldId']:
            try:
                battlefield = Battlefield.objects.get({'_id': data['battlefieldId']})
            except DoesNotExist:
                return {
                    'status': 'fail',
                    'message': 'No such channel'
                }, 404
            channel.battlefield = battlefield
        
        channel.save()
    except DoesNotExist:
        return {
            'status': 'fail',
            'message': 'No such channel'
        }, 404
    else:
        return {
            'status': 'success',
            'message': 'Successfully updated the channel properties.'
        }, 200

def get_a_players_list(channelId):
    try:
        return Channel.objects.get({'_id': int(channelId)}).participants
    except DoesNotExist:
        return None

def enter_this_channel(channelId, data):
    try:
        channel = Channel.objects.get({'_id': int(channelId)})

        # Checking number of participants
        if len(channel.participants) >= channel.maximum:
            return 'exceed'

        # Checking the name already taken
        if data['playerName'] in [d.playerName for d in channel.participants]:
            return 'duplicated'

        # Checking request has a valid jwt token(= if a new player is a signed user)
        if data['signed']['status'] == 'success':
            guest = False
        else:
            guest = True
        
        channel.participants.append(PlayerInfo(
            playerId=channel.getNextPlayerId(),
            playerName=data['playerName'],
            guest=guest,
            dateEntered=datetime.datetime.utcnow()
        ))
        channel.save()
        return 'done'
    except DoesNotExist:
        return None

def leave_this_channel(channelId, playerName):
    try:
        channel = Channel.objects.get({'_id': int(channelId)})

        target = -1
        for idx, player in enumerate(channel.participants):
            if player.playerName == playerName:
                target = idx
                break
        if target == -1:
            return 'noplayer'
        channel.participants.pop(target)
        channel.save()

        return 'done'
    except DoesNotExist:
        return None