from pymodm import fields, MongoModel

class SaveInfo(MongoModel):
    # _id = ObjectId()
    saveId = fields.IntegerField(primary_key=True)
    channelId = fields.IntegerField()
    score = fields.IntegerField()
    location = EmbeddedDocumentField(Coordinate)
    items = fields.ListField(fields=fields.CharField())
    guest = fields.BooleanField(default=True)
    guestPssword = fields.CharField()
    
    class Coordinate(MongoModel):
        x = fields.IntegerField()
        y = fields.IntegerField()

    def __repr__(self):
        return "<saveInfo '{}'".format(self.saveID)

    class Meta:
        collection_name = 'saveInfo'
        final = True