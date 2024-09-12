from django.http import JsonResponse

# Create your views here.

def tarefa_ver(request):
    if request.method == "GET":
        tarefa = {'id': 1234, 'Atividade':'Estudar backend!'}
        return JsonResponse(tarefa)

def tarefa_editar(request):
    pass
def tarefa_deletar(request):
    pass