from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.db import transaction
from accounts.models.account_models import Account, AccountType
from django.contrib.auth import get_user_model
from categories.models.category_models import Category
from categories.defaults import DEFAULT_CATEGORIES 

User = get_user_model()



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_default_user_data(sender, instance, created, **kwargs):
    if not created:
        return
    
    def on_commit():

        accounts = [
            Account(
                user=instance,
                name=label,
                account_type=account_type,
                opening_balance=0
            )
            for account_type, label in AccountType.choices
        ]
        Account.objects.bulk_create(accounts)

        categories = [
            Category(user=instance, **data)
            for data in DEFAULT_CATEGORIES
        ]
        Category.objects.bulk_create(categories)

    transaction.on_commit(on_commit)
