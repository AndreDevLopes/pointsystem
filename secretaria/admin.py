from django.contrib import admin
from .models import Secretaria


# Register your models here.
@admin.register(Secretaria)
class AdminSecretaria(admin.ModelAdmin):
    list_display = ['nome', 'hoario_da_secretaria']

    @admin.display(empty_value='???')
    def hoario_da_secretaria(self, obj):
        return f'{obj.horario_entrada} as {obj.horario_saida}'
