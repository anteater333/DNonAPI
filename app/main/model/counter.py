from pymodm import fields, MongoModel
from pymodm.errors import DoesNotExist

class Counter(MongoModel):
    """
    Counter for auto-increment
    """
    id = fields.CharField()
    reference_value = fields.MongoBaseField()
    seq = fields.IntegerField()

    @staticmethod
    def getNextSequence(name):
        try:
            rt = Counter.objects.raw({'id': name})
            rt.update(
                {'$inc': {'seq': 1}}
            )
            return rt.first().seq
        except DoesNotExist:
            new_counter = Counter(
                id=name,
                seq=0
            ).save()
            return Counter.getNextSequence(name)

    class Meta:
        collection_name = 'counters'
        final = True