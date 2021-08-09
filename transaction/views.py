from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from transaction.serializers import (TRTypeSerializer, )
from transaction.documents import Transaction, TransactionExtra


class TransactionList(APIView):
    """
    List transactions aggregated datas based on query parametrs
    """

    def get(self, request, format=None):
        data = {
            "type": request.query_params.get("type"),
            "mode": request.query_params.get("mode"),
            "merchantId": request.query_params.get("merchantId"),
        }
        serializer = TRTypeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        merchantId = data.get('merchantId')
        type_ = data.get('type')
        mode = data.get('mode')
        if merchantId:  # merchant ID
            trans = Transaction.objects.filter(merchantId=merchantId)
        else:  # all data
            trans = Transaction.objects.all()
        if type_ == 'amount':
            if mode == 'daily':
                aggregated_data = list(trans.get_daily_sum())
            elif mode == 'weekly':
                aggregated_data = list(trans.get_weekly_sum())
            else:
                aggregated_data = list(trans.get_monthly_sum())
        else:
            if mode == 'daily':
                aggregated_data = list(trans.get_daily_count())
            elif mode == 'weekly':
                aggregated_data = list(trans.get_weekly_count())
            else:
                aggregated_data = list(trans.get_monthly_count())
        return Response(aggregated_data)


class TransactionExtraList(APIView):
    """
    List transactions aggregated datas based on query parametrs
    """

    def get(self, request, format=None):
        data = {
            "type": request.query_params.get("type"),
            "mode": request.query_params.get("mode"),
            "merchantId": request.query_params.get("merchantId"),
        }
        serializer = TRTypeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        merchantId = data.get('merchantId')
        type_ = data.get('type')
        mode = data.get('mode')
        if merchantId:  # merchant ID
            trans = TransactionExtra.objects.filter(merchantId=merchantId)
        else:  # all data
            trans = TransactionExtra.objects.all()
        if type_ == 'amount':
            if mode == 'daily':
                aggregated_data = list(trans.get_daily_sum())
            elif mode == 'weekly':
                aggregated_data = list(trans.get_weekly_sum())
            else:
                aggregated_data = list(trans.get_monthly_sum())
        else:
            if mode == 'daily':
                aggregated_data = list(trans.get_daily_count())
            elif mode == 'weekly':
                aggregated_data = list(trans.get_weekly_count())
            else:
                aggregated_data = list(trans.get_monthly_count())
        return Response(aggregated_data)
