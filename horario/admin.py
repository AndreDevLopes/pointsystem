from django.contrib import admin
from .models import Semana, Dia

@admin.register(Dia)
class AdminDia(admin.ModelAdmin):
    list_display = ['dia','cargo', 'entrada', 'intervalo', 'retorno', 'saida']


@admin.register(Semana)
class AdminSemana(admin.ModelAdmin):
   list_display = ['servidor', 'horario_segunda', 'horario_terca', 'horario_quarta',
    'horario_quinta', 'horario_sexta','horario_sabado', 'horario_domingo'] 

   @admin.display(empty_value='???')
   def horario_da_secretaria(self, obj):
        return obj.servidor.usuario.first_name

   @admin.display(empty_value='???')
   def horario_segunda(self, obj):
       if(obj.segunda):
         return f'{obj.segunda.entrada} as {obj.segunda.saida}'

   @admin.display(empty_value='???')
   def horario_terca(self, obj):
       if(obj.terca):
        return f'{obj.terca.entrada} as {obj.terca.saida}'

   @admin.display(empty_value='???')
   def horario_quarta(self, obj):
       if(obj.quarta):
        return f'{obj.quarta.entrada} as {obj.quarta.saida}'

   @admin.display(empty_value='???')
   def horario_quinta(self, obj):
       if(obj.quinta):
        return f'{obj.quinta.entrada} as {obj.quinta.saida}'

   @admin.display(empty_value='???')
   def horario_sexta(self, obj):
       if(obj.sexta):
        return f'{obj.sexta.entrada} as {obj.sexta.saida}'

   @admin.display(empty_value='???')
   def horario_sabado(self, obj):
       if(obj.sabado):
        return f'{obj.sabado.entrada} as {obj.sabado.saida}'

   @admin.display(empty_value='???')
   def horario_domingo(self, obj):
       if(obj.domingo):
        return f'{obj.domingo.entrada} as {obj.domingo.saida}'

