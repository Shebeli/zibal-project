from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from transaction.views import TransactionList, TransactionExtraList

urlpatterns = [
    path('transactions/', TransactionList.as_view()),
    path('transactions_extra/', TransactionExtraList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)