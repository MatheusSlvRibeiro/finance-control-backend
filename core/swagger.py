# core/swagger.py
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Tags para organização no Swagger
USER_TAGS = ['👥 Usuários']
ACCOUNT_TAGS = ['👝 Contas']
CATEGORY_TAGS = ['🗃️ Categorias']
TRANSACTION_TAGS = ['💸 Transações']
