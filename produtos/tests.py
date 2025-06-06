# /home/ubuntu/ecommerce_monolith/produtos/tests.py

import pytest
from django.urls import reverse
from rest_framework.test import APIClient # Using DRF's test client
from decimal import Decimal
from .models import Produto

# Mark all tests in this module to use the database
pytestmark = pytest.mark.django_db

@pytest.fixture
def api_client():
    """Fixture to provide an API client instance."""
    return APIClient()

@pytest.fixture
def produto_valido_data():
    """Fixture for valid product data."""
    return {
        # ID might be auto-generated now, or we can specify if needed for update tests
        # "id": 1, 
        "titulo": "Produto de Teste Monolito",
        "descricao": "Descrição do Produto Monolito",
        "saldo": 10,
        "preco": "99.99", # Send as string, Decimal conversion handled by serializer/view
        "foto": "http://example.com/produto.jpg",
    }

def test_integration_create_list_product(api_client, produto_valido_data):
    """
    Test integration: Create a product via API and verify it appears in the list.
    This adapts the original integration test logic for the monolith.
    Assumes an endpoint exists to create/receive products, like the original /api/receber-produtos/
    or a new dedicated creation endpoint.
    """
    # 1. Create the product using the API endpoint (adapted from receber_produtos)
    # Assuming the URL name is defined in produtos/urls.py
    # Let's assume the URL name is 'receber_produtos_api' for the POST endpoint
    # and 'listar_produtos_api' for the GET endpoint based on original urls.py
    create_url = reverse("produtos:receber_produtos_api") # Requires namespace='produtos' in main urls.py include
    response_create = api_client.post(create_url, data=produto_valido_data, format='json')

    print(f"Create Status Code: {response_create.status_code}")
    print(f"Create Response Body: {response_create.content}")

    # Verify successful creation (assuming 200 or 201 based on view logic)
    assert response_create.status_code in [200, 201]
    assert response_create.json().get("status") == "sucesso"
    created_product_id = response_create.json().get("produto_id") # Get ID if returned
    assert created_product_id is not None

    # 2. Verify the product appears in the listing API
    list_url = reverse("produtos:listar_produtos_api")
    response_list = api_client.get(list_url)

    print(f"List Status Code: {response_list.status_code}")
    # print(f"List Response Body: {response_list.content}")

    assert response_list.status_code == 200
    produtos_list = response_list.json()

    # Check if the created product (by ID or title) is in the list
    found = False
    for p in produtos_list:
        # Compare relevant fields, converting price back to Decimal for comparison if needed
        if p.get("id") == created_product_id and p.get("titulo") == produto_valido_data["titulo"]:
             assert Decimal(p.get("preco")) == Decimal(produto_valido_data["preco"])
             found = True
             break
    
    assert found, f"Product with ID {created_product_id} not found in list."

    # Optional: Direct database check
    assert Produto.objects.filter(id=created_product_id).exists()
    db_product = Produto.objects.get(id=created_product_id)
    assert db_product.titulo == produto_valido_data["titulo"]

# TODO: Add tests for other apps (autenticacao, pagamentos)
# TODO: Adapt original unit tests from microservices

