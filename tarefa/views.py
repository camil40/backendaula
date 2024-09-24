from django.http import JsonResponse
from rest_framework import viewsets
from tarefa.models import Task
from tarefa.serializer import TarefaSerializers

# Create your views here.

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TarefaSerializers