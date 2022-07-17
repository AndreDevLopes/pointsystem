from rest_framework import serializers
from .models import Cidade, Estado


class CidadeSerializer(serializers.ModelSerializer):
    nome = serializers.CharField()
    estado = serializers.CharField()

    class Meta:
        model = Cidade
        fields = '__all__'


class EstadoSerializer(serializers.ModelSerializer):
    nome = serializers.CharField()
    UF = serializers.CharField()

    class Meta:
        model = Estado
        fields = '__all__'