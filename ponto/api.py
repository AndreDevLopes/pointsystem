from datetime import datetime

import pytz
from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Ponto
from .serializers import PontoSerializer


class PontoAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PontoSerializer

    def get_queryset(self):
        user = self.request.user
        UTC = pytz.timezone('america/sao_paulo')
        return Ponto.objects.filter(servidor__usuario__username=user, dia=datetime.now(UTC))


class UpdatePontoAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ponto.objects.all()
    serializer_class = PontoSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Point updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})
