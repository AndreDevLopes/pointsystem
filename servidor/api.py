from datetime import datetime
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import servidorHorarioSerializer, horasTrabalhadasSerializer,servidorSerializer
from .models import Servidor
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
        return Ponto.objects.filter(servidor__usuario__username=user, dia=datetime.now())


class ServidorAPI(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = servidorSerializer

    def get_queryset(self):
        user = self.request.user
        return Servidor.objects.filter(usuario__username=user)
