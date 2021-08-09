from datetime import datetime

import jdatetime
from rest_framework import serializers
from rest_framework_mongoengine.fields import ObjectIdField
from rest_framework_mongoengine.serializers import DocumentSerializer

from transaction.documents import Transaction
from transaction.utils import fa_month_to_str


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

