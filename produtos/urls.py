# /home/ubuntu/ecommerce_monolith/produtos/urls.py
from django.urls import path
from .views import receber_produtos_api, listar_produtos_api #, handle_send_product, send_product_page

app_name = 'produtos' # Define the namespace for this app

urlpatterns = [
    # Endpoint to receive/create products (POST)
    path('receber/', receber_produtos_api, name='receber_produtos_api'),
    # Endpoint to list products (GET)
    path('listar/', listar_produtos_api, name='listar_produtos_api'),

    # URLs from sendproduct (commented out, need integration decision)
    # path('send-page/', send_product_page, name='send_product_page'),
    # path('send-api/', handle_send_product, name='handle_send_product'),
]

