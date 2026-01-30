from django.contrib import admin
from .models.account_models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):

    """ Admin customizado para accounts """
    list_display = [
        'uuid', 'name', 'opening_balance', 'account_type', 'user', 'created_at', 'updated_at'
    ]
    list_filter = [
        'account_type', 'user', 'created_at','updated_at'
    ]
    search_fields = [
        'user', 'account_type'
    ]
    readonly_fields = [
        'uuid', 'created_at', 'updated_at'
    ]
    ordering = [
        'created_at'
    ]

    fieldsets = (
        (None, {
            'fields': ['uuid', 'name', 'opening_balance', 'account_type']
        }),
        ('Datas importantes', {
            'fields': ['created_at', 'updated_at']
        })
    )