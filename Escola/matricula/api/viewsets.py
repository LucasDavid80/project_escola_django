from rest_framework import viewsets
from matricula import models
from matricula.api import serializers


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = models.Matricula.objects.all()
    serializer_class = serializers.MatriculaSerializer


class MatriculaViewSetOut(viewsets.ModelViewSet):
    queryset = models.Matricula.objects.all()
    serializer_class = serializers.MatriculaSerializerOut
