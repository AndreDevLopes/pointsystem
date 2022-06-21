from django.db import models


class Secretaria(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class HorarioDia(models.Model):
    DIAS_SEMANA=(
        ('SEG', 'SEGUNDA'),
        ('TER', 'TERÇA'),
        ('QUA', 'QUARTA'),
        ('QUI', 'QUINTA'),
        ('SEX', 'SEXTA'),
        ('SAB', 'SABADO'),
        ('DOM', 'DOMINGO')

    )
    dia = models.CharField(max_length=100, choices=DIAS_SEMANA)
    entrada = models.TimeField(blank=True, null=True)
    intervalo = models.TimeField(blank=True, null=True)
    retorno = models.TimeField(blank=True, null=True)
    saida = models.TimeField(blank=True, null=True)
    secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE)

    def __str__(self):
        return self.dia


class MacPermitido(models.Model):
    mac = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE)

    def __str__(self):
        return self.mac