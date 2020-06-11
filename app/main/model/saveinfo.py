from pymodm import fields, MongoModel

class SaveInfo(MongoModel):
    # _id = ObjectId()
    saveID = fields.IntegerField(primary_key=True)
    channelID = fields.IntegerField()
    score = fields.IntegerField()
    location = EmbeddedDocumentField(Coordinate)
    items = fields.ListField(fields=fields.CharField())
    
    class Coordinate(MongoModel):
        x = fields.IntegerField()
        y = fields.IntegerField()