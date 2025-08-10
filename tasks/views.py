from django.shortcuts import render, get_object_or_404
from .models import Tarefa

def listar_tarefas(request):
	tarefas = Tarefa.objects.all().order_by('-criada_em')
	return render(request, 'tasks/listar_tarefas.html', {'tarefas': tarefas})

def detalhar_tarefa(request, pk):
	tarefa = get_object_or_404(Tarefa, pk=pk)
	return render(request, 'tasks/detalhar_tarefa.html', {'tarefa': tarefa})
