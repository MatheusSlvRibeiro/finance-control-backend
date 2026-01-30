from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models.account_models import Account

User = get_user_model()

class AccountInline(admin.TabularInline):
    model = Account
    extra = 0
    
@admin.register(User)
class UserAdmin(BaseUserAdmin):

    def save_model(self, request, obj, form, change):
        if not obj.username:
            obj.username = obj.email
        super().save_model(request, obj, form, change)

    """Admin customizado para User"""
    inlines = [AccountInline]
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
        ('Informações Pessoais', {
            'fields': ['uuid', 'name', 'email', 'password']
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
        ('Datas importantes', {
            'fields': ['created_at', 'updated_at']
        })
    )

    def get_queryset(self, request):
        """Filtrar apenas registros não deletados"""
        return super().get_queryset(request).filter(deleted_at__isnull=True)
