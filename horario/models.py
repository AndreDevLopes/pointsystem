from django.db import models
from servidor.models import Servidor

# Create your models here.
class Dia(models.Model):
    dia = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100, default='')
    entrada = models.TimeField(blank=True, null=True)
    intervalo = models.TimeField(blank=True, null=True)
    retorno = models.TimeField(blank=True, null=True)
    saida = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Semana(models.Model):
    servidor = models.OneToOneField(Servidor, on_delete=models.CASCADE)
    segunda = models.ForeignKey(Dia, on_delete=models.CASCADE, related_name='segundas', null=True, blank=True)
    terca = models.ForeignKey(Dia, on_delete=models.CASCADE, related_name='tercas', null=True, blank=True)
    quarta = models.ForeignKey(Dia, on_delete=models.CASCADE, related_name='quartas', null=True, blank=True)
    quinta = models.ForeignKey(Dia, on_delete=models.CASCADE, related_name='quintas', null=True, blank=True)
    sexta= models.ForeignKey(Dia, on_delete=models.CASCADE, related_name='sextas', null=True, blank=True)
    sabado = models.ForeignKey(Dia, on_delete=models.CASCADE, related_name='sabados', null=True, blank=True)
    domingo = models.ForeignKey(Dia, on_delete=models.CASCADE, related_name='domingos', null=True, blank=True)
    
    
   

