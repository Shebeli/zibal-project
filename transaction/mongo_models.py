import datetime

from mongoengine import *

class Transaction(Document):
    createdAt = DateTimeField(default=datetime.datetime.utcnow())
    amount = IntField()
    merchantId = ObjectIdField()