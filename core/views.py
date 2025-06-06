# /home/ubuntu/ecommerce_monolith/core/views.py
from django.shortcuts import render

# View for the main login page (index.html)
def index_view(request):
    return render(request, 'index.html')

# View for the products page (products.html)
def products_view(request):
    # This view might need to fetch product data from the 'produtos' app in the future
    # For now, just render the template
    return render(request, 'products.html')

# View for the cart page (carrinho.html)
def carrinho_view(request):
    return render(request, 'carrinho.html')

# View for the payment page (pagamento.html)
def pagamento_view(request):
    return render(request, 'pagamento.html')

# View for the cards management page (cartoes.html)
def cartoes_view(request):
    return render(request, 'cartoes.html')

