from pymodm import fields, MongoModel
    
class Coordinate(MongoModel):
    x = fields.IntegerField()
    y = fields.IntegerField()

    class Meta:
        final = True

class SavedInfo(MongoModel):
    # _id = ObjectId()
    savedId = fields.IntegerField(primary_key=True)
    playerName = fields.CharField()
    channelId = fields.IntegerField()
    score = fields.IntegerField()
    location = fields.EmbeddedDocumentField(model=Coordinate)
    items = fields.ListField(field=fields.CharField())
    dateSaved = fields.DateTimeField()
    guest = fields.BooleanField(default=True)
    guestPassword = fields.CharField(required=False)

    def __repr__(self):
        return "<savedInfo '{}'".format(self.savedId)

    class Meta:
        collection_name = 'savedInfo'
        final = True