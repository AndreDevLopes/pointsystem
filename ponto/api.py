from datetime import datetime

import pytz
from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Ponto
from .serializers import PontoSerializer


class PontoAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PontoSerializer

    def get_queryset(self):
        user = self.request.user
        data_inicial = self.request.query_params.get('data_inicial')
        data_final = self.request.query_params.get('data_final')
        if data_inicial and data_final:
            return Ponto.objects.filter(servidor__usuario__username=user, dia__range=(data_inicial, data_final))
        UTC = pytz.timezone('america/sao_paulo')
        return Ponto.objects.filter(servidor__usuario__username=user, dia=datetime.now(UTC))


def time_to_int(dateobj):
    total = int(dateobj.strftime('%S'))
    total += int(dateobj.strftime('%M')) * 60
    total += int(dateobj.strftime('%H')) * 60 * 60
    return total


class UpdatePontoAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ponto.objects.all()
    serializer_class = PontoSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.data.__contains__('intervalo'):
            intervalo = datetime.strptime(request.data['intervalo'], '%H:%M:%S')
            primeiro_turno_total = time_to_int(intervalo) - time_to_int(instance.entrada)
            if primeiro_turno_total < 14400:
                return Response({"message": "não contabilizado horas suficiente para intervalo"}, status=status.HTTP_400_BAD_REQUEST)

        if request.data.__contains__('retorno'):
            retorno = datetime.strptime(request.data['retorno'], '%H:%M:%S')
            primeiro_turno_total = time_to_int(retorno) - time_to_int(instance.intervalo)
            if primeiro_turno_total < 3600:
                return Response({"message": "não contabilizado a hora de intervalo"}, status=status.HTTP_400_BAD_REQUEST)

        if request.data.__contains__('saida'):
            saida = datetime.strptime(request.data['saida'], '%H:%M:%S')
            primeiro_turno_total = time_to_int(saida) - time_to_int(instance.retorno)
            if primeiro_turno_total < 14400:
                return Response({"message": "não contabilizado horas suficiente para saida"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Point updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})
