from django.contrib import admin
from .models import Servidor, Justificativa


# Register your models here.
@admin.register(Servidor)
class AdminServidor(admin.ModelAdmin):
    list_display = ['nome_do_servidor', 'cargo', 'telefone', 'nome_da_secretaria', 'setor', 'vinculo']

    @admin.display(empty_value='???')
    def nome_da_secretaria(self, obj):
        return obj.secretaria.nome

    @admin.display(empty_value='???')
    def nome_do_servidor(self, obj):
        return obj.usuario.first_name



@admin.register(Justificativa)
class AdminJustificativa(admin.ModelAdmin):
    list_display = ['nome_servidor', 'matricula', 'tipo', 'data', 'descricao', 'upload']

    @admin.display(empty_value='???')
    def nome_servidor(self, obj):
        return obj.usuario.first_name

    @admin.display(empty_value='???')
    def data(self, obj):
        return f'{obj.data_inicio} até {obj.data_final}'

    @admin.display(empty_value='???')
    def matricula(self, obj):
        return obj.usuario.username
