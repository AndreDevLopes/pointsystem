from django.db import models
from servidor.models import Servidor


# Create your models here.
class Ponto(models.Model):
    dia = models.DateField()
    entrada = models.TimeField(blank=True, null=True)
    intervalo = models.TimeField(blank=True, null=True)
    retorno = models.TimeField(blank=True, null=True)
    saida = models.TimeField(blank=True, null=True)
    servidor = models.ForeignKey(Servidor, on_delete=models.CASCADE, default=None)
