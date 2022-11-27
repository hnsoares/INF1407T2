from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100, help_text='Entre o nome')
    preco = models.DecimalField(help_text='Entre o preço',decimal_places=2, max_digits=8)
    qtd = models.IntegerField(help_text='Entre a quantidade')
    setor = models.CharField(max_length=100, help_text='Entre o setor',null=True)
    def __str__(self):
        return self.nome