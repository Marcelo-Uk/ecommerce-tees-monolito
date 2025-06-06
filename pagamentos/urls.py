# /home/ubuntu/ecommerce_monolith/pagamentos/urls.py
from django.urls import path
from .views import validar_cartao

app_name = 'pagamentos' # Define namespace

urlpatterns = [
    path('validar/', validar_cartao, name='validar_cartao'),
]

