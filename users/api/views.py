from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import (UserSerializer, UserCreateSerializer)
from core.swagger import USER_TAGS
from core.mixins.viewset_helpers import swagger_viewset_methods

User = get_user_model()

class  UserViewSet(viewsets.ModelViewSet):
    """ Viewset para gerenciar usuários """
    queryset = User.objects.filter(deleted_at__isnull=True)
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_staff']
    search_fields = ['name', 'email', 'created_at']
    ordering = ['-created_at']

    locals().update(swagger_viewset_methods(USER_TAGS, 'usuário'))

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.isAuthenticated()]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer
