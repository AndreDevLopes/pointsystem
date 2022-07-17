from rest_framework import serializers
from .models import Cidade


class EnderecoSerializer(serializers.ModelSerializer):
    nome = serializers.CharField()
    estado = serializers.CharField()

    class Meta:
        model = Cidade
        fields = '__all__'