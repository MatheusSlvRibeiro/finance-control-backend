from django.contrib import admin
from .models.transaction_models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):

    list_display = [
        'uuid', 'description', 'category', 'account', 'created_at', 'updated_at'
    ]
    list_filter = [
        'category', 'account', 'created_at', 'updated_at'
    ]
    search_fields = [
        'uuid', 'created_at', 'updated_at'
    ]
    readonly_fields = [
        'uuid', 'created_at', 'updated_at'
    ]
    ordering = [
        'created_at'
    ]

    fieldsets = (
        (None, {
            'fields': ['uuid', 'description', 'category', 'account']
        }),
        ('Datas importantes', {
            'fields': ['created_at', 'updated_at']
        })
    )
