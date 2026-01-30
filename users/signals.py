from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.db import transaction
from accounts.models.account_models import Account

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_default_accounts(sender, instance, created, **kwargs):
    if created:
        def create_accounts():
            for account_type, label in Account.AccountType.choices:
                Account.objects.create(
                    user=instance,
                    name=label,
                    account_type=account_type,
                    opening_balance=0
                )
        transaction.on_commit(create_accounts)