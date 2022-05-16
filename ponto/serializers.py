from rest_framework import serializers

from .models import Ponto
from servidor.models import Servidor


class PontoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    dia = serializers.DateField()
    entrada = serializers.TimeField(allow_null=True)
    intervalo = serializers.TimeField(allow_null=True)
    retorno = serializers.TimeField(allow_null=True)
    saida = serializers.TimeField(allow_null=True)
    servidor = serializers.CharField()

    class Meta:
        model = Ponto
        fields = '__all__'

    def create(self, validated_data):
        matricula = validated_data['servidor']
        get_servidor = Servidor.objects.get(usuario__username=matricula)
        validated_data['servidor'] = get_servidor
        ponto = Ponto.objects.create(**validated_data)
        return ponto
