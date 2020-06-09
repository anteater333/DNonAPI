import unittest
import datetime

from app.main.model.user import User
from app.main.model.counter import Counter
from app.test.base import BaseTestCase

class TestUserModel(BaseTestCase):
    
    def test_encode_auth_token(self):
        user = User(
            userId=Counter.getNextSequence('userId'),
            userName='test',
            email='test@test.com',
            dateRegistered=datetime.datetime.utcnow()
        )
        user.userPassword = 'test'
        user.save()
        auth_token = user.encode_auth_token(user.userId)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_auth_token(self):
        id = Counter.getNextSequence('userId')
        user = User(
            userId=id,
            userName='test',
            email='test@test.com',
            dateRegistered=datetime.datetime.utcnow()
        )
        user.userPassword = 'test'
        user.save()
        auth_token = user.encode_auth_token(user.userId)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(User.decode_auth_token(auth_token.decode("utf-8") ) == id)

if __name__ == '__main__':
    unittest.main()