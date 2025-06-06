# /home/ubuntu/ecommerce_monolith/autenticacao/urls.py
from django.urls import path
from .views import LoginView, LogoutView

app_name = 'autenticacao' # Define namespace

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

