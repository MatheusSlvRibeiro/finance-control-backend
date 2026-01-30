# Finance Control Backend

O Finance Control Backend é uma API RESTful desenvolvida com Django e Django REST Framework para gestão de despesas e finanças pessoais.  
Oferece endpoints para cadastro, autenticação e administração de usuários, além de integração fácil com o frontend moderno.

---

## Funcionalidades

- Modelo de usuário customizado com autenticação por e-mail
- Cadastro e gerenciamento de usuários
- Autenticação JWT (se configurado)
- Soft delete e campos de auditoria (`created_at`, `updated_at`)
- Documentação automática da API (Swagger e Redoc)
- Painel administrativo Django Admin
- Estrutura modular e escalável

---

## Requisitos

- Python 3.10+
- Django 5.x
- Django REST Framework
- drf-yasg (para documentação da API)
- SQLite (padrão) ou PostgreSQL/MySQL (recomendado para produção)

---

## Instalação

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/MatheusSlvRibeiro/finance-control-backend.git
   cd finance-control-backend
   ```

2. **Crie e ative um ambiente virtual:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Aplique as migrações:**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crie um superusuário:**
   ```sh
   python manage.py createsuperuser
   ```

6. **Inicie o servidor de desenvolvimento:**
   ```sh
   python manage.py runserver
   ```

---

## Documentação da API

- **Swagger UI:** [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- **Redoc:** [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

---

## Estrutura do Projeto

```
finance-control-backend/
├── backend/           # Configurações do projeto Django e URLs principais
├── users/             # App de usuários (models, views, serializers)
├── core/              # Utilitários, mixins, enums, etc.
├── manage.py
└── requirements.txt
```

---

## Variáveis de Ambiente

Crie um arquivo `.env` ou defina as variáveis abaixo conforme necessário:

- `SECRET_KEY`: Chave secreta do Django
- `DEBUG`: Defina como `False` em produção
- `ALLOWED_HOSTS`: Hosts/domínios permitidos

---

## Contribuindo

Pull requests são bem-vindos! Para mudanças maiores, abra uma issue para discutir o que você gostaria de modificar.

---

## Licença

Este projeto está licenciado sob a licença MIT.

---

## Autor

Matheus Slv Ribeiro  
[GitHub](https://github.com/MatheusSlvRibeiro)

---

# Finance Control Backend

Este repositório é o **backend** do projeto [Finance Control](https://github.com/MatheusSlvRibeiro/finance-control-frontend), uma solução completa para gestão de finanças pessoais.

O backend fornece uma API RESTful robusta, desenvolvida em Django e Django REST Framework, responsável por autenticação, cadastro de usuários, controle de despesas e integração com o frontend.

> **Frontend do projeto:**  
> [https://github.com/MatheusSlvRibeiro/finance-control-frontend](https://github.com/MatheusSlvRibeiro/finance-control-frontend)
