# Finance Control Backend – Estrutura Final

Este documento detalha a estrutura final do backend após a reorganização completa, seguindo padrões de arquitetura empresarial para aplicações Django.

## Estrutura de Diretórios

```
finance-control-backend/
├── accounts/                # App de contas financeiras
│   ├── api/                # Serializers, views, rotas da API
│   ├── migrations/         # Migrações do Django
│   ├── models/             # Modelos de domínio
│   ├── admin.py            # Configuração do admin
│   ├── apps.py             # Configuração do app
│   └── ...
├── categories/             # App de categorias
│   ├── api/
│   ├── migrations/
│   ├── models/
│   ├── admin.py
│   └── ...
├── users/                  # App de usuários
│   ├── api/
│   ├── migrations/
│   ├── models/
│   ├── admin.py
│   └── ...
├── core/                   # Mixins, utilitários, swagger, helpers
│   ├── mixins/
│   │   └── models.py       # Core mixins (ver abaixo)
│   └── swagger.py
├── backend/                # Configuração global do projeto Django
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── db.sqlite3              # Banco de dados local (dev)
├── manage.py               # Entrypoint Django
├── requirements.txt        # Dependências Python
├── Dockerfile              # Build do backend
└── docker-compose.yaml     # Orquestração backend + banco
```

## Core Mixins (`core/mixins/models.py`)

### `TimeStampedModel`

- Adiciona os campos `created_at`, `updated_at`, `deleted_at`
- Implementa soft delete com métodos `delete()`, `restore()`, `hard_delete()`
- Manager customizado `ActiveManager` filtra apenas objetos não deletados

### `UUIDModel`

- Substitui chave primária auto-incrementada por UUID
- Usa `uuid.uuid4()` como padrão
- Garante identificadores únicos globalmente

### `BaseModel`

- Combina `TimeStampedModel` + `UUIDModel`
- Classe base para todos os modelos da aplicação
- Herança múltipla otimizada

## Documentação da API (Swagger)

- A documentação interativa da API está disponível via Swagger UI e ReDoc.
- Os endpoints estão organizados por domínio (accounts, categories, users, etc).
- Cada rota exibe métodos, parâmetros, exemplos de request/response e códigos de status.
- Autenticação JWT disponível para rotas protegidas.

### Endpoints principais:

| Recurso    | Endpoint Base       | Métodos Disponíveis    |
| ---------- | ------------------- | ---------------------- |
| Accounts   | /api/accounts/      | GET, POST, PUT, DELETE |
| Categories | /api/categories/    | GET, POST, PUT, DELETE |
| Users      | /api/users/         | GET, POST, PUT, DELETE |
| Auth       | /api/v1/auth/token/ | POST (login JWT)       |

## 🧪 Como Testar

### 1. Instalar e Configurar

```bash
cd c:\projetos\finance-control-backend
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

### 2. Executar Servidor

```bash
python manage.py runserver
```

### 3. Acessar Documentação

- Swagger UI: `http://127.0.0.1:8000/swagger/`
- ReDoc: `http://127.0.0.1:8000/redoc/`
- Admin: `http://127.0.0.1:8000/admin/`



## Próximos Passos e Boas Práticas

1. **Testes Automatizados**: Implementar testes unitários e de integração
2. **Permissões**: Sistema de permissões por holding/fazenda
3. **Auditoria**: Log de alterações nos modelos
4. **Cache**: Redis para otimização de queries
5. **Monitoramento**: Logging e métricas de performance
6. **Deploy**: Configuração para produção com Docker

## Padrões e Boas Práticas Adotados

- Apps Django organizados por domínio de negócio
- API RESTful estruturada com Django REST Framework
- Uso de Docker e docker-compose para padronizar ambientes
- Configurações e dependências isoladas por projeto

## Observações

- O backend está pronto para deploy em ambientes Docker ou tradicionais.
- A estrutura facilita manutenção, escalabilidade e integração contínua (CI/CD).

**Última atualização**: 30 de Janeiro de 2026