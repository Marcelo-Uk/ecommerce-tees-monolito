from django.contrib import admin
from .models import Cartao
from .forms import CartaoAdminForm

@admin.register(Cartao)
class CartaoAdmin(admin.ModelAdmin):
    # Form com validações (nº do cartão, CVV, validade)
    form = CartaoAdminForm

    # Colunas da listagem
    list_display = (
        "numero_cartao_display",
        "nome_cartao",
        "data_validade",
        "saldo_debito",
        "saldo_credito",
    )
    search_fields = ("numero_cartao", "nome_cartao")
    list_filter = ("data_validade",)
    ordering = ("-id",)

    fieldsets = (
        ("Dados do Cartão", {"fields": ("numero_cartao", "nome_cartao", "data_validade", "cvv")}),
        ("Saldos", {"fields": ("saldo_debito", "saldo_credito")}),
    )

    # Exibe número do cartão mascarado
    def numero_cartao_display(self, obj):
        n = obj.numero_cartao or ""
        return f"{n[:4]} **** **** {n[-4:]}" if len(n) >= 8 else n
    numero_cartao_display.short_description = "Número do Cartão"

    # Ação opcional para criar/atualizar um cartão de teste
    actions = ["gerar_cartao_teste"]

    def gerar_cartao_teste(self, request, queryset):
        from decimal import Decimal
        Cartao.objects.get_or_create(
            numero_cartao="1234567890123456",
            nome_cartao="SOU EU MESMO",
            data_validade="12/12",
            cvv="987",
            defaults={
                "saldo_debito": Decimal("1000.00"),
                "saldo_credito": Decimal("1000.00"),
            },
        )
        self.message_user(request, "Cartão de teste criado/atualizado.")
    gerar_cartao_teste.short_description = "Criar/atualizar cartão de teste (1234 **** **** 3456)"
