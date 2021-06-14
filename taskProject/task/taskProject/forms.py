from django import forms
from .models import Quadro,Categoria, Tarefa

class QuadroForm(forms.ModelForm):

    class Meta:
        model = Quadro
        fields = ['nome', 'descricao',]



class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ('nome',)

class TarefaForm(forms.ModelForm):

    class Meta:
        model = Tarefa
        fields = ['nome', 'descricao','data_previsao_termino','categoria']
