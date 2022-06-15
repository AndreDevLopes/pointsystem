import pytz
from datetime import datetime
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
        UTC = pytz.timezone('america/sao_paulo')
        dia = datetime.now(UTC).date()
        try:
            return Ponto.objects.get(servidor=get_servidor, dia=dia)
        except Ponto.DoesNotExist:
            validated_data['servidor'] = get_servidor
            ponto = Ponto.objects.create(**validated_data)
            return ponto

    def update(self, instance, validated_data):
        if validated_data['entrada'] is not None:
            instance.entrada = validated_data['entrada']
        if validated_data['intervalo'] is not None:
            instance.intervalo = validated_data['intervalo']
        if validated_data['retorno'] is not None:
            instance.retorno = validated_data['retorno']
        if validated_data['saida'] is not None:
            instance.saida = validated_data['saida']
        instance.save()
        return instance
