from django.db import models
from uuid import uuid1

from aluno.models import Aluno
from disciplina.models import Disciplina

# Create your models here.

class Matricula(models.Model):
    aluno_ra = models.ForeignKey(Aluno, on_delete=models.CASCADE, blank=True, null=True)
    disciplina_id = models.ForeignKey(Disciplina, on_delete=models.CASCADE, blank=True, null=True)

    np1 = models.IntegerField()
    np2 = models.IntegerField()
    np3 = models.IntegerField()
    npa = models.IntegerField()
    id = models.UUIDField(primary_key=True, default=uuid1, editable=False)
