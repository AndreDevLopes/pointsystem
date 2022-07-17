from django.db import models
from endereco.models import Cidade


# Create your models here.

class Feriado(models.Model):
    TIPOS_CHOICES = [
        ('NAC', 'Nacional'),
        ('EST', 'Estadual'),
        ('MUN', 'Municipal'),
        ('FAC', 'Facultativo')
    ]
    dia = models.DateField()
    tipo = models.CharField(choices=TIPOS_CHOICES, max_length=3, default=None)
    nome = models.CharField(max_length=200, default=None)
    endereco = models.ManyToManyField(Cidade)

    def __str__(self):
        return self.nome
