from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tarefas, name='listar_tarefas'),
    path('tarefa/<int:pk>/', views.detalhar_tarefa, name='detalhar_tarefa'),
    path('tarefa/nova/', views.criar_tarefa, name='criar_tarefa'),
    path('tarefa/<int:pk>/editar/', views.editar_tarefa, name='editar_tarefa'),
    path('tarefa/<int:pk>/excluir/', views.excluir_tarefa, name='excluir_tarefa'),
]