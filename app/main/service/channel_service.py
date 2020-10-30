import datetime

from app.main.model.channel import Channel
from app.main.model.counter import Counter
from pymodm.errors import DoesNotExist
from pymongo.errors import DuplicateKeyError

def save_new_channel(data):
    if data['maximum'] < 8 or data['maximum'] > 32:
        response_object = {
            'status': 'fail',
            'message': 'The maximum number of players should be at least 8 and less than 32.'
        }
        return response_object, 409

    new_channel = Channel(
        channelId=Counter.getNextSequence('channelId'),
        maximum=data['maximum']
    )
    try:
        new_channel.save()
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