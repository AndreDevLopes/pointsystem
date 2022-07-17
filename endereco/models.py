from django.db import models


# Create your models here.
class Estado(models.Model):
    nome = models.CharField(max_length=30)
    UF = models.CharField(max_length=2)

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome