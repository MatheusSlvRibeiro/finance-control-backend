from rest_framework import serializers
from users.models.user_models import User
from categories.models.category_models import Category, CategoryColor, CategoryIcon, CategoryType
class CategoryCreateSerializer(serializers.ModelSerializer):

    queryset=User.objects.filter(is_active=True)

    category_type = serializers.ChoiceField(
        choices=CategoryType.choices
    )
    category_color = serializers.ChoiceField(
        choices=CategoryColor.choices
    )
    category_icon = serializers.ChoiceField(
        choices=CategoryIcon.choices
    )

    class Meta:
        model = Category
        fields = (
            'uuid', 
            'name', 
            'category_type',
            'category_color', 
            'category_icon',
        )
        read_only_fields = ['uuid']

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'uuid', 
            'name', 
            'category_type', 
            'category_color', 
            'category_icon',
        )
        read_only_fields = fields