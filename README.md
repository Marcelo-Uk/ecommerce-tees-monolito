# 🧱 O Monolito – E-commerce Django

Plataforma de e-commerce desenvolvida com Django, REST Framework e integração de frontend com templates e estáticos.  
Projeto educacional criado por desenvolvedores do IFG — "os Guris".

---

## 🚀 Tecnologias Utilizadas

- Python 3.11+
- Django 5+
- Django REST Framework
- SQLite3
- HTML5, CSS3, JavaScript (Vanilla)
- JWT Authentication

---

## 📦 Requisitos

- Python 3.11 ou superior
- Git
- (Opcional) Ambiente virtual: `venv`

---

## 🔧 Passos para Executar o Projeto

### 1. Clone o Repositório

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

### 2. Crie e Ative um Ambiente Virtual

python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

### 3. Instale as Dependências

pip install -r requirements.txt

    Se o arquivo requirements.txt não existir, você pode gerá-lo com:

pip freeze > requirements.txt

### 4. Configure as Migrações

python manage.py makemigrations
python manage.py migrate

### 5. Crie um Superusuário

python manage.py createsuperuser

### 6. Rode o Servidor Local

python manage.py runserver

### 7. Acesse no Navegador

    Frontend: http://localhost:8000

    Admin: http://localhost:8000/admin
