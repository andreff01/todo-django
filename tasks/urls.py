from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tarefas, name='listar_tarefas'),
    path('tarefa/<int:pk>/', views.detalhar_tarefa, name='detalhar_tarefa'),
]
