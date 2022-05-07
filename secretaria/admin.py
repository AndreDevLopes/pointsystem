from django.contrib import admin
from .models import Secretaria


# Register your models here.
@admin.register(Secretaria)
class AdminSecretaria(admin.ModelAdmin):
    list_display = ['nome', 'horario_da_secretaria', 'horario_do_intervalo_da_secretaria']

    @admin.display(empty_value='???')
    def horario_da_secretaria(self, obj):
        return f'{obj.entrada} as {obj.saida}'

    @admin.display(empty_value='???')
    def horario_do_intervalo_da_secretaria(self, obj):
        return f'{obj.intervalo} as {obj.retorno}'
