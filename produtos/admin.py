# produtos/admin.py
from django.contrib import admin
from .models import Produto
from django.utils.html import format_html

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "preco", "saldo", "foto", "foto_preview")
    search_fields = ("titulo", "descricao")
    list_filter = ("preco",)

    def foto_preview(self, obj):
        if obj.foto:
            return format_html('<img src="{}" width="60"/>', obj.get_foto_url())
        return "-"
    foto_preview.short_description = "Imagem"
