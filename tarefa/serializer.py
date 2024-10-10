from tarefa.models import Task, Comment, Tag, Notification, FileUpload, Usuario
from rest_framework import serializers

class TarefaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ComentarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ListaComentarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment_text','fk_user', 'fk_task']

class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        
class ListaTagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class NotificacaoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        
class FileUploadSerializers(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = '__all__'
        
class ListaUsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

