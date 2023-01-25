from rest_framework import serializers
from aluno import models

from estagio.api.serializers import EstagioSerializer


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Aluno
        fields = '__all__'


class AlunoSerializerOut(serializers.ModelSerializer):
    estagio_id = EstagioSerializer()

    class Meta:
        model = models.Aluno
        fields = '__all__'