from pymodm import fields, MongoModel, validators

from app.main.model.battlefield import Battlefield
# from app.main.model.user import User

class MaxRangeException(Exception):
    pass

class PlayerInfo(MongoModel):
    playerName = fields.CharField()
    highscore = fields.IntegerField(default=0)
    signed = fields.BooleanField()

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

    class Meta:
        collection_name = 'channels'
        final = True
