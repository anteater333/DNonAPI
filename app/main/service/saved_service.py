import string, datetime
from random import choice

from app.main.model.savedinfo import SavedInfo, Coordinate
from app.main.model.counter import Counter
from app.main.model.user import User
from app.main.model.channel import Channel

from pymodm.errors import DoesNotExist, ValidationError
from pymongo.errors import DuplicateKeyError

def save_game_progress(data):
    try:
        Channel.objects.get({'_id': data['channelId']})
    except DoesNotExist:
        return {
            'status': 'fail',
            'message': 'Can not find such channel'
        }, 404

    new_save = SavedInfo(
        savedId = Counter.getNextSequence('savedId'),
        channelId = data['channelId'],
        playerName = data['playerName'],
        score = data['score'],
        location = Coordinate(
            x = data['location']['x'],
            y = data['location']['y']
        ),
        items = data['items'],
        dateSaved = datetime.datetime.utcnow(),
        guest = data['guest']
    )

    try:
        if not data['guest']:
            otp = ''.join(choice(string.digits) for _ in range(4)) # random 4 digits
            new_save.guestPassword = otp
            new_save.save()

            return {
                'status': 'success',
                'message': 'Successfully saved.',
                'data': {
                    'savedId': new_save.savedId,
                    'otp': otp
                }
            }, 201
        else:
            user = User.objects.get({'_id': data['userId']})

            for idx, saved in enumerate(user.savedData):
                if saved.channelId == data['channelId']:
                    user.savedData[idx] = new_save
                    user.save()
                    return {
                        'status': 'success',
                        'message': 'Successfully saved. The previous game data has been replaced.',
                        'data': {
                            'savedId': new_save.savedId
                        }
                    }, 200

            user.savedData.append(new_save)
            user.save()
            return {
                'status': 'success',
                'message': 'Successfully saved',
                'data': {
                    'savedId': new_save.savedId
                }
            }, 201
    except DoesNotExist:
        return {
            'status': 'fail',
            'message': 'Can not find such user'
        }, 404

def load_guest_game_progress(savedId, otp):
    try:
        saved_data = SavedInfo.objects.get({'_id':int(savedId)})
        saved_data.delete()
        return saved_data
    except DoesNotExist:
        return None

def load_user_game_progress(savedId, userName):
    try:
        user = User.objects.get({'userName':userName})

        target = -1
        for idx, saved in enumerate(user.savedData):
            if saved.savedId == int(savedId):
                target = idx
                break

        if target == -1:
            return None
        saved_data = user.savedData[target]
        user.savedData.pop(target)
        user.save()
        return saved_data
    except DoesNotExist:
        return None