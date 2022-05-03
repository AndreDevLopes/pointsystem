from django.db import models
from django.contrib.auth.models import User
from secretaria.models import Secretaria


# Create your models here.
class Servidor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    CPF = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15)
    cargo = models.CharField(max_length=200)
    secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.first_name


