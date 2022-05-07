from django.db import models


# Create your models here.
class Secretaria(models.Model):
    nome = models.CharField(max_length=200)
    entrada = models.TimeField(blank=True, null=True)
    intervalo = models.TimeField(blank=True, null=True)
    retorno = models.TimeField(blank=True, null=True)
    saida = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.nome
