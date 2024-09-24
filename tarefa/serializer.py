from tarefa.models import Tarefa
from rest_framework import serializers

class TarefaSerializers(serializers.ModelSerializer):
    class Meta:
        model =Tarefa
        fields = '__all__'
