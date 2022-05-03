from django.db import models


# Create your models here.
class Secretaria(models.Model):
    nome = models.CharField(max_length=200)
    horario_entrada = models.TimeField()
    horario_saida = models.TimeField()

    def __str__(self):
        return self.nome
