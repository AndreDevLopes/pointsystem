from datetime import datetime

import pytz
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import servidorHorarioSerializer, horasTrabalhadasSerializer, servidorSerializer,\
    JustificativaSerializer
from .models import Servidor, Justificativa
from ponto.models import Ponto


class HorarioServidorAPI(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = servidorHorarioSerializer

    def get_queryset(self):
        user = self.request.user
        return Servidor.objects.filter(usuario__username=user)


class HorasTrabalhadaAPI(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = horasTrabalhadasSerializer

    def get_queryset(self):
        user = self.request.user
        UTC = pytz.timezone('america/sao_paulo')
        return Ponto.objects.filter(servidor__usuario__username=user, dia=datetime.now(UTC))


class ServidorAPI(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = servidorSerializer

    def get_queryset(self):
        user = self.request.user
        return Servidor.objects.filter(usuario__username=user)


class JustificativaAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JustificativaSerializer

    def get_queryset(self):
        user = self.request.user
        return Justificativa.objects.filter(servidor__usuario__username=user)