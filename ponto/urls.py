from django.urls import path
from .api import PontoAPI, UpdatePontoAPIView
urlpatterns = [
    path('', PontoAPI.as_view()),
    path('update/<int:pk>/', UpdatePontoAPIView.as_view())
]
