from pymodm import fields, MongoModel

from app.main.model.battlefield import Battlefield
from app.main.model.user import User

class Channel(MongoModel):
    # _id = ObjectId()
    channelId = fields.IntegerField(primary_key=True)
    ranking = fields.ListField(field=fields.CharField())
    maximum = fields.IntegerField()
    battlefield = fields.EmbeddedDocumentField(Battlefield)
    participants = fields.EmbeddedDocumentListField(User)

    class Meta:
        collection_name = 'channels'
        final = True
