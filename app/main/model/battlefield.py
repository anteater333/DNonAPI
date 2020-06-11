from pymodm import fields, MongoModel

class Battlefield(MongoModel):
    # _id = ObjectId()
    BattlefieldID = fields.IntegerField(primary_key=True)
    description = fields.CharField()
    geography = fields.ListField(field=fields.ListField(field=fields.IntegerField()))