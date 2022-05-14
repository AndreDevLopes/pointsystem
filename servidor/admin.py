from django.contrib import admin
from .models import Servidor


# Register your models here.
@admin.register(Servidor)
class AdminServidor(admin.ModelAdmin):
    list_display = ['nome_do_servidor', 'matricula', 'cargo', 'telefone', 'nome_da_secretaria']

    @admin.display(empty_value='???')
    def nome_da_secretaria(self, obj):
        return obj.secretaria.nome

    @admin.display(empty_value='???')
    def nome_do_servidor(self, obj):
        return obj.usuario.first_name
