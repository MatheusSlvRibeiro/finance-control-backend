from core.mixins.models import BaseModel
from django.db import models
from django.conf import settings


class AccountType(models.TextChoices):
    CHECKING = 'checking', 'Conta corrente'
    WALLET = 'wallet', 'Carteira'
    INVESTMENTS = 'investments', 'Investimentos'

class Account(BaseModel):

    name = models.CharField(
        max_length=100, 
        verbose_name='Nome'
    )

    opening_balance = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        default=0, 
        verbose_name='Saldo inicial'
    )
    
    account_type = models.CharField(
        max_length=20,
        choices=AccountType.choices,
        blank=True,
        verbose_name='Tipo de conta'
    )

    # Relacionamentos

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='accounts',
        verbose_name='Usuário',
    )

    class Meta:
        db_table = 'account'
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'
        permissions = [
            ('can_view_account', 'Can_view_account'),
            ('can_edit_account', 'Can_edit_account'),
            ('can_delete_account', 'Can_delete_account'),            
        ]

    def __str__(self):
        return f"{self.name} ({self.user})"