from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.models import ProtectedError


class TimeStampedModel(models.Model):
    """
    Modelo abstrato que adiciona campos de timestamp e soft delete
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name='Deletado em')

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        """
        Soft delete - marca o registro como deletado sem remover do banco
        """
        try:
            # Verificar se há relacionamentos protegidos
            self._check_can_delete()
        except ProtectedError as e:
            raise ValidationError(
                "Este registro não pode ser excluído pois está sendo usado em outro lugar."
            )
        
        self.deleted_at = timezone.now()
        self.save(using=using, update_fields=['deleted_at'])
        return self

    def hard_delete(self, using=None, keep_parents=False):
        """
        Hard delete - remove permanentemente do banco de dados
        """
        return super().delete(using=using, keep_parents=keep_parents)

    def restore(self):
        """
        Restaura um registro que foi soft deleted
        """
        self.deleted_at = None
        self.save(update_fields=['deleted_at'])
        return self

    def is_deleted(self):
        """
        Verifica se o registro foi soft deleted
        """
        return self.deleted_at is not None

    def _check_can_delete(self):
        """
        Verifica se o objeto pode ser deletado (implementar em subclasses se necessário)
        """
        pass

    @classmethod
    def get_active_objects(cls):
        """
        Retorna apenas objetos não deletados
        """
        return cls.objects.filter(deleted_at__isnull=True)

    @classmethod
    def get_deleted_objects(cls):
        """
        Retorna apenas objetos deletados
        """
        return cls.objects.filter(deleted_at__isnull=False)


class UUIDModel(models.Model):
    """
    Modelo abstrato que adiciona UUID como chave primária
    """
    import uuid
    uuid = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False,
        verbose_name='UUID'
    )

    class Meta:
        abstract = True


class BaseModel(UUIDModel, TimeStampedModel):
    """
    Modelo base que combina UUID e TimeStamped
    """
    class Meta:
        abstract = True
