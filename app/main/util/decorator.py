from functools import wraps
from flask import request

from app.main.service.auth_helper import Auth

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:   # not token == fail
            return data, status
        
        return f(*args, **kwargs)
    
    return decorated

def prove_yourself(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')
        if not token:
            return data, status
        if kwargs['userName'] != token.get('userName'):
            response_object = {
                'status': 'fail',
                'message': 'unauthorized access'
            }
            return response_object, 401
        return f(*args, **kwargs)
    return decorated

# 관리자 기능 예
def admin_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.get_logged_in_user(request)

        token = data.get('data')
        if not token:
            return data, status
        
        admin = token.get('admin')
        if not admin:
            response_object = {
                'status': 'fail',
                'message': 'admin token required'
            }
            return response_object, 401

        return f(*args, **kwargs)

    return decorated