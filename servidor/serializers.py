from rest_framework import serializers
from .models import Servidor, Justificativa
from secretaria.models import Secretaria, HorarioDia
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
