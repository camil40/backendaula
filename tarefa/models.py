from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tarefa(models.Model):
    name = models.CharField(max_length=255)
    descricao = models.TextField(null=True,blank=True )
    data_inicio = models.DateField(null=True,blank=True)
    data_finalizar = models.DateTimeField(null=True,blank=True)
    finalizada = models.BooleanField(default=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

