from django.http import JsonResponse
from rest_framework import viewsets, generics
from tarefa.models import Task, Comment, Tag, Notification, FileUpload
from tarefa.serializer import TarefaSerializers, ComentarioSerializers, TagSerializers, NotificacaoSerializers, FileUploadSerializers, ListaComentarioSerializers, ListaTagSerializers

# Create your views here.

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TarefaSerializers
    
class TarefaRetrieveView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TarefaSerializers
    
class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = ComentarioSerializers

class ListaComentarioTask(generics.ListAPIView):
    '''Lista de comentarios por uma task'''
    def get_queryset(self):
        queryset = Comment.objects.filter(fk_task=self.kwargs['pk'])
        return queryset
    serializer_class = 	ListaComentarioSerializers

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers
    
class ListaTagTask(generics.ListAPIView):
    '''Lista de tags por uma task'''
    def get_queryset(self):
        queryset = Tag.objects.filter(tasks=self.kwargs['pk'])
        return queryset
    serializer_class = 	ListaTagSerializers

class NotificacaoViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificacaoSerializers
    
class FileUploadViewSet(viewsets.ModelViewSet):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializers