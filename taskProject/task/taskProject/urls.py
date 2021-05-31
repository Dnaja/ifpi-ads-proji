from django.urls import path
from . import views
from django.template.response import TemplateResponse


urlpatterns = [
    path('', views.index,name = 'index'),
    path('quadro/cadastro/', views.cadastro_quadro,name = 'cadastro_quadro'),
    path('quadro/editar/<int:id>/', views.editar_quadro, name='editar_quadro'),
    path('quadro/excluir/<int:id>/', views.excluir_quadro, name='excluir_quadro'),
    path('categoria/cadastrar/', views.cadastro_categoria, name='cadastro_categoria'),
    path('categoria/', views.exibir_categoria, name='exibir_categoria'),
    path('categoria/editar/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('categoria/excluir/<int:id>/', views.excluir_categoria, name='excluir_categoria'),
]


