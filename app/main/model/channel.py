from pymodm import fields, MongoModel, validators

from app.main.model.battlefield import Battlefield
# from app.main.model.user import User

class MaxRangeException(Exception):
    pass

class PlayerInfo(MongoModel):
    playerId = fields.IntegerField(primary_key=True, required=True)
    playerName = fields.CharField()
    highscore = fields.IntegerField(default=0)
    guest = fields.BooleanField()
    dateEntered = fields.DateTimeField()

    class Meta:
        final = True

class Channel(MongoModel):
    # _id = ObjectId()
    channelId = fields.IntegerField(primary_key=True, required=True)
    maximum = fields.IntegerField(max_value=32, min_value=8)
    battlefield = fields.EmbeddedDocumentField(Battlefield)
    ranking = fields.ListField(
        field=fields.EmbeddedDocumentField(PlayerInfo)
    )
    participants = fields.ListField(
        field=fields.EmbeddedDocumentField(PlayerInfo)
    )
    playerCount = fields.IntegerField(default=0)

    def getNextPlayerId(self):
        self.playerCount += 1
        return self.playerCount

    class Meta:
        collection_name = 'channels'
        final = True
