from pymodm import fields, MongoModel

# from app.main.model.channel import Channel

class GameLog(MongoModel):
    # _id = ObjectId()
    logId = fields.IntegerField(primary_key=True)
    killLogs = fields.ListField(fields=fields.CharField())
    score = fields.CharField()
    
    channel = fields.ReferenceField('channels')
    
    rank = fields.IntegerField()

    class Meta:
        collection_name = 'gameLogs'
        final = True