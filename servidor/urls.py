from django.urls import path
from .api import HorarioServidorAPI, HorasTrabalhadaAPI, ServidorAPI
urlpatterns = [
    path('', ServidorAPI.as_view()),
    path('horario/', HorarioServidorAPI.as_view()),
    path('horas/trabalhadas/', HorasTrabalhadaAPI.as_view())
]
