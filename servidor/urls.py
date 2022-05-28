from django.urls import path
from .api import HorarioServidorAPI, HorasTrabalhadaAPI
urlpatterns = [
    path('horario/', HorarioServidorAPI.as_view()),
    path('horas/trabalhadas/', HorasTrabalhadaAPI.as_view())
]
