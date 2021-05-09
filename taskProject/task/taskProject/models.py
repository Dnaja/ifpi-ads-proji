from django.db import models

class Quadro(models.Model):

    nome = models.CharField(max_length=30, null=False)
    descricao = models.CharField(max_length=200, null=True , blank=True)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.nome
