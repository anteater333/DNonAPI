from pymodm import fields, MongoModel
    
class Coordinate(MongoModel):
    x = fields.IntegerField()
    y = fields.IntegerField()

class SaveInfo(MongoModel):
    # _id = ObjectId()
    saveId = fields.IntegerField(primary_key=True)
    channelId = fields.IntegerField()
    score = fields.IntegerField()
    location = fields.EmbeddedDocumentField(model=Coordinate)
    items = fields.ListField(field=fields.CharField())
    guest = fields.BooleanField(default=True)
    guestPssword = fields.CharField(required=False)

    def __repr__(self):
        return "<saveInfo '{}'".format(self.saveID)

    class Meta:
        collection_name = 'saveInfo'
        final = True