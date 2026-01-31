from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import (TransactionSerializer, TransactionCreateSerializer)
from core.mixins.viewset_mixins import (
    CreateAllowAnyMixin,
    CreateSerializerMixin
)
from core.swagger import TRANSACTION_TAGS
from core.mixins.viewset_helpers import swagger_viewset_methods
from transactions.models.transaction_models import Transaction
class TransactionViewSet(
    CreateAllowAnyMixin,
    CreateSerializerMixin,
    viewsets.ModelViewSet
):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    create_serializer_class = TransactionCreateSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', 'category', 'date']
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    locals().update(swagger_viewset_methods(TRANSACTION_TAGS, 'Contas'))