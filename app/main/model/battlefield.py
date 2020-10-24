from pymodm import fields, MongoModel

class Battlefield(MongoModel):
    # _id = ObjectId()
    battlefieldId = fields.IntegerField(primary_key=True)
    battlefieldName = fields.CharField()
    description = fields.CharField()
    geography = fields.ListField(field=fields.ListField(field=fields.IntegerField()))
    check = fields.CharField()

    class Meta:
        collection_name = 'battlefields'
        final = True