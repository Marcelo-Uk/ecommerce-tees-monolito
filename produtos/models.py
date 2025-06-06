# produtos/models.py
from django.db import models

class Produto(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    saldo = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.CharField(max_length=100)  # Apenas o nome do arquivo (ex: imagem.png)

    def __str__(self):
        return self.titulo

    def get_foto_url(self):
        return f"/static/assets/imgs/{self.foto}"
