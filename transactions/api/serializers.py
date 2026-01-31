from rest_framework import serializers
from transactions.models.transaction_models import Transaction
from categories.models.category_models import CategoriesList


class TransactionCreateSerializer(serializers.ModelSerializer):

    category = serializers.ChoiceField(
        choices=CategoriesList.choices
    )

    class Meta:
        model = Transaction
        fields = (
            'uuid', 
            'description', 
            'category',
            'value',
            'date',
            'account'
        )
        read_only_fields = ['uuid']

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = (
            'uuid', 
            'description', 
            'category',
            'value',
            'date',
            'account'
        )
        read_only_fields = fields