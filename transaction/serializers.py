from datetime import datetime

from rest_framework import serializers
from rest_framework_mongoengine.fields import ObjectIdField

from transaction.documents import Transaction


class TRTypeSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=([
        ('amount', 'مقدار'),
        ('count', 'تعداد')
    ]))
    mode = serializers.ChoiceField(choices=([
        ('daily', 'روزانه'),
        ('weekly', 'هفتگی'),
        ('monthly', 'ماهانه')
    ]))
    merchantId = ObjectIdField(required=False, allow_null=True)

