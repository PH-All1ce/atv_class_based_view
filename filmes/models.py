from django.db import models

# Create your models here.


class Filme(models.Model):
    nome = models.CharField()
    duracao = models.IntegerField()
    lancamento = models.DateField()
    genero = models.CharField()
    diretor = models.CharField()

    def __str__(self):
        return self.nome