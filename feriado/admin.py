from django.contrib import admin
from .models import Feriado


# Register your models here.
@admin.register(Feriado)
class AdminFeriados(admin.ModelAdmin):
    list_display = ['nome', 'dia', 'tipo', 'cidades']

    def cidades(self, obj):
        return "\n".join([e.nome for e in obj.endereco.all()])
