from django.contrib import admin
from .models import Estado, Cidade


# Register your models here.
@admin.register(Estado)
class AdminEstado(admin.ModelAdmin):
    list_display = ['nome', 'UF']


@admin.register(Cidade)
class AdminCidade(admin.ModelAdmin):
    list_display = ['nome', 'estado']
