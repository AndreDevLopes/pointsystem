from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import FeriadoSerializer
from .models import Feriado


class FeridoAPI(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FeriadoSerializer

    def get_queryset(self):
        data_inicial = self.request.query_params.get('data_inicial')
        data_final = self.request.query_params.get('data_final')
        if data_inicial and data_final:
            return Feriado.objects.filter(dia__range=(data_inicial, data_final))

        return Feriado.objects.all()
