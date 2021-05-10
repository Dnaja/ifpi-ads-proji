from django.shortcuts import render,redirect
from .forms import QuadroForm,CategoriaForm
from .models import Quadro,Categoria

def index(request):
    quadros = Quadro.objects.all()
    return render(request, 'taskProject/index.html',{'quadros':quadros})

def cadastro_quadro(request):
    if request.method == "POST":
        form = QuadroForm(request.POST)
        nome = request.POST['nome']
        buscar_repetido = Quadro.objects.filter(nome = nome)
        if form.is_valid():
            if len(buscar_repetido) > 0:
                return redirect('cadastro_quadro')
            else:
                form.save()
                return redirect('index')

    #else:
        #form = QuadroForm()
    return render(request,'taskProject/criar_quadro.html')

def editar_quadro(request,id):
    if request.method == "POST":
        quadro = Quadro.objects.get(pk = id)
        form = QuadroForm(request.POST, instance=quadro)
        buscar_repetido = Quadro.objects.filter(nome=quadro.nome)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        quadro = Quadro.objects.filter(id = id)
        print(quadro[0].id)
        return render(request, 'taskProject/editar_quadro.html',
                      {'quadro_id':id,
                       'quadro': quadro[0]
                       })
    #return render(request,'taskProject/criar_quadro.html')

def excluir_quadro(request,id):
    #quadro = Quadro.objects.get(pk = id)
    quadro = Quadro.objects.filter(pk=id).delete()
    return redirect('index')


def cadastro_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        nome = request.POST['nome']
        buscar_repetido = Categoria.objects.filter(nome=nome)
        if form.is_valid():
            if len(buscar_repetido) > 0:
                return redirect('cadastro_categoria')
            form.save()
            return redirect('exibir_categoria')

    #else:
        #form = QuadroForm()
    return render(request,'taskProject/criar_categoria.html')


def exibir_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'taskProject/exibir_categoria.html',{'categorias':categorias})

def editar_categoria(request,id):
    if request.method == "POST":
        categoria = Categoria.objects.get(pk = id)
        form = CategoriaForm(request.POST, instance=categoria)
        buscar_repetido = Categoria.objects.filter(nome=categoria.nome)
        if form.is_valid():
            if len(buscar_repetido) > 0:
                return redirect('exibir_categoria')
            form.save()
            return redirect('exibir_categoria')

    else:
        categoria = Categoria.objects.filter(id = id)
        print(categoria[0].id)
        return render(request, 'taskProject/editar_categoria.html',
                      {'categoria_id':id,
                       'categoria': categoria[0]
                       })
    #return render(request,'taskProject/criar_quadro.html')

def excluir_categoria(request,id):
    categoria = Categoria.objects.filter(pk=id).delete()
    return redirect('exibir_categoria')