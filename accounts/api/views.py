from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import (AccountSerializer, AccountCreateSerializer)
from core.swagger import ACCOUNT_TAGS
from core.mixins.viewset_helpers import swagger_viewset_methods
from accounts.models.account_models import Account

class AccountViewSet(viewsets.ModelViewSet):

    serializer_class = AccountSerializer
    permissions_classes = [permissions.IsAdminUser]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', 'account_type']
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    locals().update(swagger_viewset_methods(ACCOUNT_TAGS, 'Contas'))

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return AccountCreateSerializer
        return AccountSerializer