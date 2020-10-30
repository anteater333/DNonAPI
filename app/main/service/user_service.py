import datetime

from app.main.model.user import User
from app.main.model.counter import Counter
from pymodm.errors import DoesNotExist
from pymongo.errors import DuplicateKeyError

def save_new_user(data):
    new_user = User(
        userId=Counter.getNextSequence('userId'),
        userName=data['userName'],
        email=data['email'],
        dateRegistered=datetime.datetime.utcnow()
    )
    new_user.userPassword = data['userPassword']    
    try:
        new_user.save()
    except DuplicateKeyError:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.'
        }
        return response_object, 409     # 409 status : Conflict
    else:
        return generate_token(new_user)

def get_all_users():
    return list(User.objects.all())

def get_a_user(userName):
    try:
        return User.objects.get({'userName': userName})
    except DoesNotExist:
        return None

def delete_a_user(userName):
    try:
        user = User.objects.get({'userName': userName})
        user.delete()
        return user
    except DoesNotExist:
        return None

def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.userId)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401