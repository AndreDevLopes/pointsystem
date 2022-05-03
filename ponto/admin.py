from django.contrib import admin
from .models import Ponto


# Register your models here.
@admin.register(Ponto)
class AdminPonto(admin.ModelAdmin):
    list_display = ['servidor', 'dia', 'entrada', 'intervalo', 'retorno', 'saida']
