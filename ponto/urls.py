from django.urls import path
from .api import PontoAPI
urlpatterns = [
    path('', PontoAPI.as_view()),
]
