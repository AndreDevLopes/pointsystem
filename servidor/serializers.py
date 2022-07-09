from datetime import time

from rest_framework import serializers
from .models import Servidor, Justificativa
from secretaria.models import Secretaria, HorarioDia
from ponto.models import Ponto
from django.contrib.auth.models import User


class secretariaSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    nome = serializers.CharField(read_only=True)
    horarios = serializers.SerializerMethodField()

    def get_horarios(self, obj):
        horarios = HorarioDia.objects.filter(secretaria=obj)
        horarioDias = []
        for horario in horarios:
            obj = {
                "dia": horario.dia,
                "entrada": horario.entrada,
                "intervalo": horario.intervalo,
                "retorno": horario.retorno,
                "saida": horario.saida
            }
            horarioDias.append(obj)

        return horarioDias

    class Meta:
        model = Secretaria
        fields = '__all__'


class servidorHorarioSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    usuario = serializers.CharField(read_only=True)
    secretaria = secretariaSerializer()

    class Meta:
        model = Servidor
        fields = '__all__'


def time_to_int(dateobj):
    total = int(dateobj.strftime('%S'))
    total += int(dateobj.strftime('%M')) * 60
    total += int(dateobj.strftime('%H')) * 60 * 60
    return total


class horasTrabalhadasSerializer(serializers.ModelSerializer):
    dia = serializers.CharField(read_only=True)
    horas_trabalhadas = serializers.SerializerMethodField()

    def get_horas_trabalhadas(self, obj):
        valor_entrada = time(00, 00, 00)
        valor_intervalo = time(00, 00, 00)
        valor_retorno = time(00, 00, 00)
        valor_saida = time(00, 00, 00)

        if obj.entrada is not None:
            valor_entrada = obj.entrada
        if obj.intervalo is not None:
            valor_intervalo = obj.intervalo
        if obj.retorno is not None:
            valor_retorno = obj.retorno
        if obj.saida is not None:
            valor_saida = obj.saida

        horas_primeiro_turno = time_to_int(valor_intervalo) - time_to_int(valor_entrada)
        horas_segundo_turno = time_to_int(valor_saida) - time_to_int(valor_retorno)
        horas_trabalhadas = horas_primeiro_turno + horas_segundo_turno

        if horas_primeiro_turno <= 0:
            return 0
        if horas_segundo_turno <= 0:
            return horas_primeiro_turno

        return horas_trabalhadas

    class Meta:
        model = Ponto
        fields = ('dia', 'horas_trabalhadas',)


class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'is_active', 'is_staff', 'email', 'is_superuser', 'last_login')


class servidorSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    usuario = usuarioSerializer()
    vinculo = serializers.CharField(read_only=True)
    setor = serializers.CharField(read_only=True)
    telefone = serializers.CharField(read_only=True)
    cargo = serializers.CharField(read_only=True)
    secretaria = secretariaSerializer()

    class Meta:
        model = Servidor
        fields = '__all__'


class JustificativaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    tipo = serializers.CharField(max_length=100)
    data_inicio = serializers.DateField()
    data_final = serializers.DateField()
    descricao = serializers.CharField()
    servidor = serializers.CharField()
    arquivo = serializers.FileField(required=False)

    class Meta:
        model = Justificativa
        fields = '__all__'

    def create(self, validated_data):
        matricula = validated_data['servidor']
        get_servidor = Servidor.objects.get(usuario__username=matricula)
        validated_data['servidor'] = get_servidor
        justificativa = Justificativa.objects.create(**validated_data)
        return justificativa
