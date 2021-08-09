from datetime import datetime

from mongoengine import (Document, DateTimeField, IntField,
                         ObjectIdField, QuerySet)
from django.conf import settings

from transaction.manager import TransactionQuerySet


class AbstractTransaction(Document):
    createdAt = DateTimeField(default=datetime.utcnow)
    amount = IntField(required=True)
    merchantId = ObjectIdField()  # or reference field to document

    meta = {
        'abstract': True,
        'queryset_class': TransactionQuerySet,
        'ordering': ['-createdAt']
    }


class Transaction(AbstractTransaction):

    def save(self, *args, **kwargs):
        if self.objects.is_overload():
            self.switch_collection('transaction_extra')
            return super().save(*args, **kwargs)
        return super().save(*args, **kwargs)


class TransactionExtra(AbstractTransaction): # to access the extra collection
    pass
