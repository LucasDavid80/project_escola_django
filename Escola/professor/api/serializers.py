from rest_framework import serializers
from professor import models

from disciplina.api.serializers import DisciplinaSerializer


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Professor
        fields = '__all__'


class ProfessorSerializerOut(serializers.ModelSerializer):
    disciplina_id = DisciplinaSerializer()

    class Meta:
        model = models.Professor
        fields = '__all__'