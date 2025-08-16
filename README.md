#### E-commerce Monolito (Django)

Pequeno e-commerce monolítico em Django que lista produtos, possui carrinho e pagamento (cartão “fake” em dev). O frontend é servido pelos próprios templates do Django e a API expõe endpoints REST simples.

📦 Stack

Python 3.11+ (recomendado)

Django 5.x

Django REST Framework

SimpleJWT (auth via tokens, opcional)

django-cors-headers

SQLite (dev)

Static files servidos pelo Django em DEBUG=True

✅ Pré-requisitos

Python 3.11+

pip atualizado (python -m pip install --upgrade pip)

(Opcional) venv para isolar dependências


#### 1) Clone o repositório  - USE O MINGW64
git clone https://github.com/Marcelo-Uk/ecommerce-tees-monolito.git
cd ecommerce-tees-monolito

#### 2) Crie e ative um ambiente virtual (recomendado) - USE O MINGW64
python -m venv .venv

#### Windows  - USE O MINGW64
source venv/Scripts/activate

#### 3) Instale as dependências
pip install -r requirements.txt
#### (se não existir requirements.txt, instale manualmente:)
#### pip install "Django>=5.0,<6" djangorestframework djangorestframework-simplejwt django-cors-headers

🗃️ Configuração rápida

O projeto já vem com DEBUG=True e banco SQLite configurado em settings.py.
Você não deve versionar o arquivo db.sqlite3.

#### 4) Aplique as migrações
python manage.py migrate

#### 5) Crie um superusuário para acessar o /admin (opcional, mas útil)
python manage.py createsuperuser

▶️ Rodando

python manage.py runserver


Acesse: http://127.0.0.1:8000/


#### Para adicionar produtos:

Acesse /admin com o superusuário.

Em Produtos, cadastre alguns produtos.

A imagem é apenas o nome do arquivo (ex.: vga-1.png -- confira na pasta o nome das imgs), que deve existir em static/assets/imgs/.

Em Cartões, cadastre um cartão (nº, nome, validade MM/AA, CVV) e saldos.


