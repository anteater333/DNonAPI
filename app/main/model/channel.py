from pymodm import fields, MongoModel

class Channel(MongoModel):
    # _id = ObjectId()
    channelID = fields.IntegerField(primary_key=True)
    battlefield = fields.EmbeddedDocumentField(Battlefield)
    ranking = fields.ListField(field=fields.CharField())
    participants = fields.EmbeddedDocumentListField(User)
    maximum = fields.IntegerField()