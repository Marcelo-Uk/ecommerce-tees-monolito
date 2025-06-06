# /home/ubuntu/ecommerce_monolith/produtos/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Produto
from decimal import Decimal # Import Decimal for potential price handling

# Function to handle saving/updating product data (refactored from receber_produtos)
# This can be called internally now instead of via HTTP POST
def save_or_update_product(product_data):
    try:
        # Ensure price is handled correctly as Decimal
        price = Decimal(product_data.get('preco', 0))

        # Use update_or_create based on 'id' if provided and unique.
        # If ID is auto-generated or not provided, use create().
        if 'id' in product_data:
             produto, created = Produto.objects.update_or_create(
                 id=product_data['id'],
                 defaults={
                     'titulo': product_data.get('titulo', ''),
                     'descricao': product_data.get('descricao', ''),
                     'saldo': int(product_data.get('saldo', 0)),
                     'preco': price,
                     'foto': product_data.get('foto', ''),
                 }
             )
             return {'status': 'sucesso', 'mensagem': f'Produto {"criado" if created else "atualizado"} com sucesso!', 'produto_id': produto.id}
        else:
            # Handle creation if no ID is provided
            produto = Produto.objects.create(
                 titulo=product_data.get('titulo', ''),
                 descricao=product_data.get('descricao', ''),
                 saldo=int(product_data.get('saldo', 0)),
                 preco=price,
                 foto=product_data.get('foto', ''),
            )
            return {'status': 'sucesso', 'mensagem': 'Produto criado com sucesso!', 'produto_id': produto.id}

    except Exception as e:
        # Log the error
        print(f"Error saving product: {e}")
        return {'status': 'erro', 'mensagem': str(e)}

# Original API endpoint to receive products via POST (might be deprecated in monolith)
# Kept for reference or potential external integration if needed, but internal calls should use save_or_update_product
@csrf_exempt
def receber_produtos_api(request):
    if request.method == 'POST':
        try:
            dados = json.loads(request.body)
            result = save_or_update_product(dados)
            status_code = 200 if result['status'] == 'sucesso' else 400
            return JsonResponse(result, status=status_code)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'erro', 'mensagem': 'Dados JSON inválidos'}, status=400)
        except Exception as e:
            # Log the error
            print(f"Error in receber_produtos_api: {e}")
            return JsonResponse({'status': 'erro', 'mensagem': 'Erro interno no servidor'}, status=500)
    else:
        return JsonResponse({'status': 'erro', 'mensagem': 'Método não permitido'}, status=405)

# API endpoint to list products
def listar_produtos_api(request):
    if request.method == 'GET':
        try:
            produtos = Produto.objects.all().values('id', 'titulo', 'descricao', 'saldo', 'preco', 'foto')
            return JsonResponse(list(produtos), safe=False)
        except Exception as e:
            # Log the error
            print(f"Error in listar_produtos_api: {e}")
            return JsonResponse({'status': 'erro', 'mensagem': 'Erro ao listar produtos'}, status=500)
    else:
        return JsonResponse({'status': 'erro', 'mensagem': 'Método não permitido'}, status=405)

# Views from micro_sendproduto are commented out as they need further integration decisions and templates.
# from django.shortcuts import render
# @csrf_exempt
# def send_product_page(request):
#     # Need to move/create the template 'produtos/sendprodutos.html'
#     # return render(request, 'produtos/sendprodutos.html')
#     pass # Placeholder for now

# @csrf_exempt
# def handle_send_product(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)
#             print(f"Produto recebido do formulário: {data}") # Log
#             result = save_or_update_product(data) # Call internal function
#             status_code = 200 if result['status'] == 'sucesso' else 400
#             # Redirect or return JSON depending on frontend needs
#             return JsonResponse(result, status=status_code)
#         except json.JSONDecodeError:
#             return JsonResponse({"erro": "Dados inválidos enviados."}, status=400)
#         except Exception as e:
#             print(f"Error in handle_send_product: {e}")
#             return JsonResponse({"erro": "Erro interno ao processar produto."}, status=500)
#     else:
#         return JsonResponse({"erro": "Método não permitido."}, status=405)

