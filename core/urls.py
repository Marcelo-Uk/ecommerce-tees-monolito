# /home/ubuntu/ecommerce_monolith/core/urls.py
from django.urls import path
from . import views

app_name = 'core' # Define namespace

urlpatterns = [
    path('', views.index_view, name='index'), # Root path for login page
    path('products/', views.products_view, name='products'),
    path('carrinho/', views.carrinho_view, name='carrinho'),
    path('pagamento/', views.pagamento_view, name='pagamento'),
    path('cartoes/', views.cartoes_view, name='cartoes'),
]

