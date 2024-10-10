from django.http import JsonResponse
from rest_framework import viewsets, generics
from tarefa.models import Task, Comment, Tag, Notification, FileUpload, Usuario
from tarefa.serializer import TarefaSerializers, ComentarioSerializers, TagSerializers, NotificacaoSerializers, FileUploadSerializers, ListaComentarioSerializers, ListaTagSerializers, ListaUsuarioSerializers
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TarefaSerializers
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class TarefaRetrieveView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TarefaSerializers
    
class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = ComentarioSerializers
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaComentarioTask(generics.ListAPIView):
    '''Lista de comentarios por uma task'''
    def get_queryset(self):
        queryset = Comment.objects.filter(fk_task=self.kwargs['pk'])
        return queryset
    serializer_class = 	ListaComentarioSerializers
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ListaTagTask(generics.ListAPIView):
    '''Lista de tags por uma task'''
    def get_queryset(self):
        queryset = Tag.objects.filter(tasks=self.kwargs['pk'])
        return queryset
    serializer_class = 	ListaTagSerializers
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    

class NotificacaoViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificacaoSerializers
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class FileUploadViewSet(viewsets.ModelViewSet):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializers
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    
class ListaUsuarioTask(generics.ListAPIView):
    '''Lista de usuarios por uma task'''
    def get_queryset(self):
        queryset = Usuario.objects.filter(task=self.kwargs['pk'])
        return queryset
    serializer_class = 	ListaUsuarioSerializers
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]