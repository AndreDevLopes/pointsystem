from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import servidorHorarioSerializer, servidorSerializer,\
    JustificativaSerializer
from .models import Servidor, Justificativa



class HorarioServidorAPI(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = servidorHorarioSerializer

    def get_queryset(self):
        user = self.request.user
        return Servidor.objects.filter(usuario__username=user)



class ServidorAPI(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = servidorSerializer

    def get_queryset(self):
        user = self.request.user
        return Servidor.objects.filter(usuario__username=user)


class ServidoresAPI(ListAPIView):
    serializer_class = servidorSerializer

    def get_queryset(self):
        return Servidor.objects.all()


class JustificativaAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JustificativaSerializer

    def get_queryset(self):
        user = self.request.user
        return Justificativa.objects.filter(servidor__usuario__username=user)