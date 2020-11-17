from app.main.model.user import User
from ..service.blacklist_service import save_token

from pymodm.errors import DoesNotExist

class Auth:

    @staticmethod
    def login_user(data):
        try:
            # fetch the user data
            user = User.objects.get({'email': data.get('email')})
            if user.check_userPassword(data.get('password')):
                auth_token = user.encode_auth_token(user.userId)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': user.userName,
                        'Authorization': auth_token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'Wrong password.'
                }
                return response_object, 401
        except DoesNotExist:
            response_object = {
                'status': 'fail',
                'message': 'There is no such email.'
            }
            return response_object, 401
        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500
    
    @staticmethod
    def logout_user(data):
        auth_token = data
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                try:
                    user = User.objects.get({'_id': resp})
                except DoesNotExist:
                    response_object = {
                        'status': 'fail',
                        'message': 'Provide a valid auth token.'
                    }
                    return response_object, 401
                else:
                    response_object = {
                        'status': 'success',
                        'data': {
                            'userId': user.userId,
                            'userName': user.userName,
                            'email': user.email,
                            'dateRegistered': str(user.dateRegistered),
                            'admin': user.admin
                        }
                    }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401