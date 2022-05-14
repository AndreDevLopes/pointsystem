from django.contrib import admin
from .models import Ponto
from import_export.admin import ExportMixin


# Register your models here.
@admin.register(Ponto)
class AdminPonto(ExportMixin, admin.ModelAdmin):
    list_display = ['nome_do_servidor', 'dia', 'entrada', 'intervalo', 'retorno', 'saida']
    list_filter = (
        'dia',
    )

    @admin.display(empty_value='???')
    def nome_do_servidor(self, obj):
        return obj.servidor.usuario.first_name