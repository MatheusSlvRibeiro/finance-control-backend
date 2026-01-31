from rest_framework import serializers
from accounts.models.account_models import Account, AccountType

class AccountCreateSerializer(serializers.ModelSerializer):

    account_type = serializers.ChoiceField(
        choices=AccountType.choices
    )

    class Meta:
        model = Account
        fields = ('uuid', 'name', 'opening_balance', 'account_type')
        read_only_fields = ['uuid']

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = (
            'uuid',
            'name',
            'opening_balance',
            'account_type',
            'created_at',
            'updated_at'
        )
        read_only_fields = fields