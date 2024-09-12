from django.contrib import admin
from tarefa.models import Tarefa

# Register your models here.
class Tarefas(admin.ModelAdmin):
    list_display = ('id','name', 
                    'descricao', 
                    'data_inicio',
                    'data_finalizar',
                    'finalizada', 
                    'usuario')
    list_display_links = ('id', 'name')

admin.site.register(Tarefa, Tarefas)