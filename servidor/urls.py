from django.urls import path
from .api import HorarioServidorAPI, HorasTrabalhadaAPI, ServidorAPI, JustificativaAPI
urlpatterns = [
    path('', ServidorAPI.as_view()),
    path('horario/', HorarioServidorAPI.as_view()),
    path('horas/trabalhadas/', HorasTrabalhadaAPI.as_view()),
    path('justificativa/', JustificativaAPI.as_view())
]
