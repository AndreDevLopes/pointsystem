from django.urls import path
from .api import FeridoAPI
urlpatterns = [
    path('', FeridoAPI.as_view()),
]
