from django.urls import path
from .api import CreatePontoAPI
urlpatterns = [
    path('', CreatePontoAPI.as_view()),
]
