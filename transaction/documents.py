from datetime import datetime

from mongoengine import (Document, DateTimeField, IntField,
                         ObjectIdField, queryset_manager)
from django.conf import settings


class AbstractTransaction(Document):
    createdAt = DateTimeField(default=datetime.utcnow)
    amount = IntField(required=True)
    merchantId = ObjectIdField()  # or reference field to document

    meta = {
        'abstract': True,
        'ordering': ['-createdAt']
    }

# class TransactionExtra(AbstractTransaction):
#     """Uses the same document and schema to store data"""
#     pass


class Transaction(AbstractTransaction):

    # might need to add this method to queryset
    @classmethod
    def is_overload(cls):
        return cls.objects.count() > settings.MAX_TRANSACTION_COUNT

    def save(self, *args, **kwargs):
        if self.is_overload():
            self.switch_collection('transaction_extra')
            return super().save(*args, **kwargs)
        return super().save(*args, **kwargs)
