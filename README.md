# Finance Control Backend

Uma API REST robusta desenvolvida em Django para o ecossistema Finance Control, fornecendo funcionalidades essenciais para gestão de finanças pessoais e integração com frontend moderno.

## 📋 Índice

- [Sobre o Projeto](#🚀-sobre-o-projeto)
- [Tecnologias Utilizadas](#🛠-tecnologias-utilizadas)
- [Pré-requisitos](#📋-pré-requisitos)
- [Instalação](#🔧-instalação)
- [Configuração](#⚙️-configuração)
- [Banco de Dados](#🗄️-banco-de-dados)
- [Execução](#🚀-execução)
- [Desenvolvimento](#💻-desenvolvimento)
- [API Documentation](#📚-api-documentation)
- [Testes](#🧪-testes)
- [Deploy](#🚀-deploy)
- [Contribuição](#🤝-contribuição)
- [Licença](#📄-licença)
- [Notas Técnicas Futuras](#notas-técnicas-futuras)
- [Changelog](#changelog)
- [Estrutura Completa do Projeto](#estrutura-completa-do-projeto)

## 🚀 Sobre o Projeto

O Finance Control Backend é uma API REST desenvolvida em Django que fornece a base para aplicações de controle financeiro. Este projeto oferece:

- **Autenticação JWT**: Sistema robusto de autenticação com tokens JWT
- **API RESTful**: Endpoints bem estruturados seguindo padrões REST
- **Documentação Automática**: Swagger/OpenAPI integrado para documentação da API
- **Banco SQLite (dev) / PostgreSQL (prod)**: Persistência de dados flexível
- **Extensibilidade**: Arquitetura modular para fácil adição de novas funcionalidades

## 🛠 Tecnologias Utilizadas

- **Django 5.2.4**
- **Django REST Framework**
- **drf-yasg** (Swagger/OpenAPI)
- **djangorestframework-simplejwt** (JWT)
- **django-filter**
- **SQLite** (padrão) / **PostgreSQL** (produção)
- **Python 3.13+**

## 📋 Pré-requisitos

- Python 3.13 ou superior
- SQLite (padrão) ou PostgreSQL 12+
- Git

## 🔧 Instalação

1. **Clone o repositório**

   ```sh
   git clone https://github.com/MatheusSlvRibeiro/finance-control-backend.git
   cd finance-control-backend
   ```

2. **Crie e ative o ambiente virtual**

   ```sh
   python -m venv venv
   venv\Scripts\activate  # Windows
   # ou
   source venv/bin/activate  # Linux/Mac
   ```

3. **Instale as dependências**
   ```sh
   pip install -r requirements.txt
   ```

## ⚙️ Configuração

1. **Crie o arquivo de variáveis de ambiente `.env`** (opcional, se desejar customizar)

   ```
   SECRET_KEY=sua-chave-secreta
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

2. **Configure o banco de dados em `backend/settings.py` se for usar PostgreSQL**

## 🗄️ Banco de Dados

1. **Aplique as migrações**

   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Crie um superusuário**
   ```sh
   python manage.py createsuperuser
   ```

## 🚀 Execução

```sh
python manage.py runserver
```

Acesse: [http://localhost:8000](http://localhost:8000)

## 💻 Desenvolvimento

- Estrutura modular por apps: `accounts`, `categories`, `users`, `core`
- Uso de mixins para DRY e boas práticas
- Soft delete, UUID, timestamps em todos os modelos

## 📚 API Documentation

- **Swagger UI**: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- **ReDoc**: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

### Exemplo de uso da API

```bash
# Obter token JWT
curl -X POST http://localhost:8000/api/v1/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

## 🧪 Testes

```sh
python manage.py test
```

## 🚀 Deploy

- Pronto para deploy tradicional ou via Docker.
- Exemplo de build Docker disponível no projeto.

## 🤝 Contribuição

Pull requests são bem-vindos! Para mudanças maiores, abra uma issue para discutir o que você gostaria de modificar.

## 📄 Licença

MIT

## Notas Técnicas Futuras

- Implementar testes automatizados
- Sistema de permissões avançado
- Auditoria de alterações
- Cache com Redis
- Monitoramento e logging
- Deploy com Docker em produção

## Changelog

- **2026-01-30**: Estrutura empresarial, documentação Swagger, modularização, soft delete, UUID, melhorias de segurança e escalabilidade.

---

## Estrutura Completa do Projeto

Consulte a estrutura detalhada e padrões de arquitetura em [ESTRUTURA.md](ESTRUTURA.md).
