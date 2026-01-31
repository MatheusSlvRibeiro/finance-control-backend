from django.contrib import admin
from .models.category_models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):


    list_display = [
        'uuid', 'name', 'category_type', 'category_icon', 'category_color', 'user', 'created_at', 'updated_at'
    ]
    list_filter = [
        'category_type', 'user', 'created_at', 'updated_at'
    ]
    search_fields = [
        'user', 'category_type',
    ]
    readonly_fields = [
        'uuid', 'created_at', 'updated_at'
    ]
    ordering = [
        'created_at'
    ]

    fieldsets = (
        (None, {
            'fields': ['uuid', 'name', 'category_type', 'category_icon', 'category_color', 'user']
        }),
        ('Datas importantes', {
            'fields': ['created_at', 'updated_at']
        })
    )