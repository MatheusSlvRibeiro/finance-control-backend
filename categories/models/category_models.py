from django.db import models
from core.mixins.models import BaseModel
from django.conf import settings


class CategoryType(models.TextChoices):
    INCOME = 'income', 'Receitas'
    EXPENSE = 'expense', 'Despesas'


class CategoryColor(models.TextChoices):
    GREEN = 'green', 'Verde'
    DARKGREEN = 'darkgreen', 'Verde Escuro'
    BLUE = 'blue', 'Azul'
    ORANGE = 'orange', 'Laranja'
    BROWN = 'brown', 'Marrom'
    GRAY = 'gray', 'Cinza'
    RED = 'red', 'Vermelho'
    PURPLE = 'purple', 'Roxo'


class CategoryIcon(models.TextChoices):
    BRIEFCASE = 'briefcase', 'Maleta'
    TRENDINGUP = 'trendingup', 'Investimentos'
    LAPTOP = 'laptop', 'Laptop'
    HOME = 'home', 'Casa'
    UTENSILS = 'utensils', 'Utensílios'
    BUS = 'bus', 'Ônibus'
    WRENCH = 'wrench', 'Ferramenta'
    HEARTPULSE = 'heartpulse', 'Saúde'
    PARTYPOPPER = 'partypopper', 'Lazer'
    

class CategoriesList(models.TextChoices):
    WORK = 'work', 'Trabalho'
    INVESTMENTS = 'investments', 'Investimentos'
    FREELANCE = 'freelance', 'Freelance'
    HOME = 'home', 'Moradia'
    FOOD = 'food', 'Alimentação'
    TRANSPORT = 'transport', 'Transporte'
    SERVICES = 'services', 'Serviços'
    HEALTHY = 'healthy', 'Saúde'
    LEISURE = 'leisure', 'Lazer'



class Category(BaseModel):
    name = models.CharField(
        max_length=100,
        verbose_name='Nome'
    )
    category_type = models.CharField(
        max_length=20,
        choices=CategoryType.choices,
        blank=False,
        verbose_name='Tipo de Categoria',
    )
    category_color = models.CharField(
        max_length=10,
        choices=CategoryColor.choices,
        blank=False,
        verbose_name='Cor da categoria'
    )
    category_icon = models.CharField(
        max_length=20,
        choices=CategoryIcon.choices,
        blank=False,
        verbose_name='Icone da categoria'
    )

    # Relacionamentos

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='categories',
        verbose_name='Usuário'
    )

    class Meta:
        db_table ='category'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        permissions = [
            ('can_view_category', 'Can_view_category'),
            ('can_edit_category', 'Can_edit_category'),
            ('can_delete_category', 'Can_delete_category'),
        ]

    def __str__(self):
        return super().__str__()