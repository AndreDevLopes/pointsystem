from django.db import models
from django.contrib.auth.models import User
from secretaria.models import Secretaria


# Create your models here.
class Servidor(models.Model):
    VINCULO_CHOICES = (
        ('CONC', 'CONCURSADO'),
        ('CONT', 'CONTRATADO'),
        ('CARG', 'CARGO.COMISSION'),
        ('EFET', 'EFET.COMISSIONA'),
        ('PENS', 'PENSIONISTA'),
        ('CARGE', 'CARGO ELETIVO'),
        ('INAT', 'INATIVO'),
        ('PENS', 'PENSAO POR MORT'),
        ('SERV', 'SERVIDOR CEDIDO')
    )
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    vinculo = models.CharField(max_length=5, choices=VINCULO_CHOICES, null=True, blank=True)
    setor = models.CharField(max_length=150, null=True, blank=True)
    telefone = models.CharField(max_length=15)
    cargo = models.CharField(max_length=200)
    secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.first_name


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.usuario.id, filename)


class Justificativa(models.Model):
    STATUS_CHOICES = (
        ('PEN', 'PENDENTE'),
        ('APR', 'APROVADO'),
        ('REP', 'REPROVADO')
    )
    tipo = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_final = models.DateField()
    descricao = models.TextField()
    upload = models.FileField(upload_to=user_directory_path, null=True, blank=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='PEN')
