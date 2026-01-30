from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager  
from django.db import models
from core.mixins.models import BaseModel
import uuid

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O email é obrigatório")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password) 
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser  must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser, BaseModel):
    """Usuário customizado baseado em AbstractUser"""
    name = models.CharField(max_length=200, verbose_name='Nome')
    email = models.EmailField(unique=True, verbose_name='E-mail')

    # Configurar email como campo de login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']

    objects = UserManager()
    
    class Meta:
        db_table = 'user'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        permissions = [
            ('can_view_user', 'Can_view_user'),
            ('can_edit_user', 'Can_edit_user'),
            ('can_delete_user', 'Can_edit_user'),
        ]
    
    def __str__(self):
        return"{self.name} ({self.email})"
    