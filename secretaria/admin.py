from django.contrib import admin
from .models import Secretaria, HorarioDia, MacPermitido


# Register your models here.
@admin.register(Secretaria)
class AdminSecretaria(admin.ModelAdmin):
    list_display = ['nome']


@admin.register(HorarioDia)
class AdminHorarioDia(admin.ModelAdmin):
    list_display = ['secretaria', 'dia', 'entrada', 'intervalo', 'retorno', 'saida']


@admin.register(MacPermitido)
class AdminMacPermitido(admin.ModelAdmin):
    list_display = ['mac', 'modelo', 'secretaria', 'is_active']
    list_filter = ('modelo', 'secretaria')

