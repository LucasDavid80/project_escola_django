from rest_framework import serializers
from matricula import models

from aluno.api.serializers import AlunoSerializer
from disciplina.api.serializers import DisciplinaSerializer


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Matricula
        fields = '__all__'


class MatriculaSerializerOut(serializers.ModelSerializer):
    aluno_ra = AlunoSerializer()
    disciplina_id = DisciplinaSerializer()

    class Meta:
        model = models.Matricula
        fields = '__all__'