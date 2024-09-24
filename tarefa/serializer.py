from tarefa.models import Task
from rest_framework import serializers

class TarefaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
