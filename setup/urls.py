"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tarefa.views import TarefaViewSet, TarefaRetrieveView, ComentarioViewSet, TagViewSet, NotificacaoViewSet, FileUploadViewSet, ListaComentarioTask, ListaTagTask
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Tarefa', TarefaViewSet, basename='Tarefa')
router.register('Comentarios', ComentarioViewSet, basename='Comentarios')
router.register('Tags', TagViewSet, basename='Tags')
router.register('Notificações', NotificacaoViewSet, basename='Notificacoes')
router.register('FileUploads', FileUploadViewSet, basename='FileUploads')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('Tarefa/<int:pk>/',TarefaRetrieveView.as_view(), name="tarefa=retrieve"),
    path('Tarefa/<int:pk>/comentarios/', ListaComentarioTask.as_view()),
    path('Tarefa/<int:pk>/tags/', ListaTagTask.as_view())
]
