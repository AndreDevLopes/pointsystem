from datetime import datetime
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Ponto
from .serializers import PontoSerializer


class PontoAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PontoSerializer

    def get_queryset(self):
        user = self.request.user
        return Ponto.objects.filter(servidor__usuario__username=user, dia=datetime.now())






