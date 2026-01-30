from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User = get_user_model()

@admin.register(User)
class UserAdmin(BaseUserAdmin):

    """Admin customizado para User"""
    list_display = [
        'uuid', 'name', 'email', 'is_active', 'is_staff', 'created_at', 'updated_at'
    ]
    list_filter = [
        'is_active', 'is_staff', 'created_at', 'updated_at', 'is_superuser'
    ]
    search_fields = [
        'email', 'name', 'last_name'
    ]
    readonly_fields = [
        'uuid', 'created_at', 'updated_at', 'last_login'
    ]
    ordering = [
        'created_at'
    ]

    """ Campos para exibição no formulário"""
    fieldsets = (
        (None, {
            'fields': ['uuid', 'email', 'password']
        }),
        ('Informações Pessoais', {
            'fields': ['name']
        }),
        ('Permissões', {
            'fields': ['is_staff', 'is_active', 'is_superuser']
        }),
        ('Datas importantes', {
            'fields': ['created_at', 'updated_at', 'last_login']
        }),
    )

    """Campos para criação de usuário"""
    add_fieldsets = (
        (None, {
            'classes': ['wide',],
            'fields': ['email', 'name', 'password1', 'password2', 'is_active'],
        }),
    )

    def get_queryset(self, request):
        """Filtrar apenas registros não deletados"""
        return super().get_queryset(request).filter(deleted_at__isnull=True)
