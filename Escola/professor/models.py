from django.db import models
from uuid import uuid1

from disciplina.models import Disciplina

# Create your models here.

class Professor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid1, editable=False)
    nome = models.CharField(max_length=45)
    ano_nascimento = models.IntegerField()
    cpf = models.CharField(max_length=14)
    cidade = models.CharField(max_length=45)
    bairro = models.CharField(max_length=45)
    rua = models.CharField(max_length=45)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=200)

    disciplina_id = models.ForeignKey(Disciplina, on_delete=models.CASCADE, blank=True, null=True)
