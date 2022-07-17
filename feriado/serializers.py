from rest_framework import serializers
from .models import Feriado


class FeriadoSerializer(serializers.ModelSerializer):
    dia = serializers.DateField()
    tipo = serializers.CharField()
    nome = serializers.CharField()

    class Meta:
        model = Feriado
        fields = ('dia', 'tipo', 'nome')
