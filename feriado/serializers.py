from rest_framework import serializers
from .models import Feriado
from endereco.serializers import EnderecoSerializer


class FeriadoSerializer(serializers.ModelSerializer):
    dia = serializers.DateField()
    tipo = serializers.CharField()
    nome = serializers.CharField()
    endereco = EnderecoSerializer(many=True)

    class Meta:
        model = Feriado
        fields = '__all__'
