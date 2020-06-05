from pymodm import fields, MongoModel
from pymodm.errors import DoesNotExist

from app.main.model.counter import Counter

import datetime

class BlacklistToken(MongoModel):
    """
    Token Model for storing JWT tokens
    """
    id = fields.IntegerField(primary_key=True)
    token = fields.CharField(required=True)
    blacklisted_on = fields.DateTimeField(required=True)

    def __init__(self, token):
        super().__init__()  # manually call parent's initializer.
        self.token = token
        self.blacklisted_on = datetime.datetime.now()
        self.id = Counter.getNextSequence('blacklistId')

    def __repr__(self):
        return '<id: token: {}'.format(self.token)
    
    @staticmethod
    def check_blacklist(auth_token):
        # check whetehr auth token has been blacklisted
        try:
            BlacklistToken.objects.get({'token':str(auth_token)})
        except DoesNotExist:
            return False
        else:
            return True

    class Meta:
        collection_name = 'blacklistTokens'
        final = True