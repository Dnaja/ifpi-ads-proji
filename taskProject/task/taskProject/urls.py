from django.urls import path
from . import views
from django.template.response import TemplateResponse


urlpatterns = [
    path('', views.index,name = 'index'),
    path('quadro/cadastro/', views.cadastro_quadro,name = 'cadastro_quadro'),
    path('quadro/editar/<int:id>/', views.editar_quadro, name='editar_quadro'),
    path('quadro/excluir/', views.excluir_quadro, name='excluir_quadro'),
    path('quadro/<int:id>/tarefas/', views.listar_tarefas, name='listar_tarefas'),
    path('categoria/cadastrar/', views.cadastro_categoria, name='cadastro_categoria'),
    path('categoria/', views.exibir_categoria, name='exibir_categoria'),
    path('categoria/editar/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('categoria/excluir/', views.excluir_categoria, name='excluir_categoria'),
    path('tarefa/cadastro/', views.cadastro_tarefa, name='cadastro_tarefa'),
    path('tarefa/<int:id>', views.visualizar_modal_form, name='visualizar_modal_form')
]


