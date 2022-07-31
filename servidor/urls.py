from django.urls import path
from .api import HorarioServidorAPI, ServidorAPI, JustificativaAPI, ServidoresAPI
urlpatterns = [
    path('', ServidorAPI.as_view()),
    path('list/', ServidoresAPI.as_view()),
    path('horario/', HorarioServidorAPI.as_view()),
    path('justificativa/', JustificativaAPI.as_view())
]
