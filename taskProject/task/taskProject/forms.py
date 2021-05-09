from django import forms
from .models import Quadro,Categoria

class QuadroForm(forms.ModelForm):

    class Meta:
        model = Quadro
        fields = ['nome', 'descricao',]



class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ('nome',)
