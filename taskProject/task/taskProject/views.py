from django.shortcuts import render,redirect,reverse
from .forms import QuadroForm,CategoriaForm, TarefaForm
from .models import Quadro,Categoria, Tarefa
from django.contrib import messages

def index(request):
    quadros = Quadro.objects.all()
    return render(request, 'taskProject/index.html',{'quadros':quadros})

def cadastro_quadro(request):
    if request.method == "POST":
        form = QuadroForm(request.POST)
        nome = request.POST['nome']
        buscar_repetido = Quadro.objects.filter(nome__iexact = nome).count()
        if form.is_valid():
            if buscar_repetido > 0:
                messages.warning(request,"Quadro já existe!")
                return redirect('index')
            else:
                form.save()
                messages.success(request,"Quadro cadastrado")
                return redirect('index')

    #else:
        #form = QuadroForm()
    return render(request,'taskProject/criar_quadro.html')

def editar_quadro(request,id):
    if request.method == "POST":
        quadro = Quadro.objects.get(pk = id)
        form = QuadroForm(request.POST, instance=quadro)
        buscar_repetido = Quadro.objects.filter(nome__iexact=request.POST['nome']).exclude(pk = id).count()
        print(buscar_repetido)
        if form.is_valid():
            if (buscar_repetido > 0):
                messages.warning(request,"Quadro já cadastrado")
                return redirect('index')
            form.save()
            messages.success(request,"Quadro alterado")
            return redirect('index')

    else:
        quadro = Quadro.objects.filter(id = id)
        return render(request, 'taskProject/editar_quadro.html',
                      {'quadro_id':id,
                       'quadro': quadro[0]
                       })
    #return render(request,'taskProject/criar_quadro.html')



def excluir_quadro(request):
    print(request.POST)
    if request.method == "POST":
            quadro = Quadro.objects.filter(pk=request.POST['quadro_id']).delete()
            messages.success(request,"Quadro excluído!")
            return redirect('index')


def cadastro_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        nome = request.POST['nome']
        buscar_repetido = Categoria.objects.filter(nome__iexact = nome).count()
        if form.is_valid():
            if buscar_repetido > 0:
                messages.warning(request,"Categoria já existe!")
                return redirect('exibir_categoria')
            form.save()
            messages.success(request,"Categoria criada com sucesso!")
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
        buscar_repetido = Categoria.objects.filter(nome__iexact=request.POST['nome']).exclude(pk = id).count()
        print(buscar_repetido)
        if form.is_valid():
            if buscar_repetido > 0:
                messages.warning(request,"Categoria já existe!")
                return redirect('exibir_categoria')
            form.save()
            messages.success(request,"Categoria alterada!")
            return redirect('exibir_categoria')

    else:
        categoria = Categoria.objects.filter(id = id)
        print(categoria[0].id)
        return render(request, 'taskProject/editar_categoria.html',
                      {'categoria_id':id,
                       'categoria': categoria[0]
                       })
    #return render(request,'taskProject/criar_quadro.html')


def excluir_categoria(request):
    if request.method == "POST":
        print(request.POST)
        categoria = Categoria.objects.filter(pk=request.POST['categoria_id']).delete()
        messages.success(request,"Categoria excluída!")
        return redirect('exibir_categoria')

def cadastro_tarefa(request):
    if request.method == "POST":
        form = TarefaForm(request.POST)
        nome = request.POST['nome']
        buscar_repetido = Tarefa.objects.filter(nome__iexact = nome).count()
        if form.is_valid():
            if buscar_repetido > 0:
                messages.warning(request,"Nome da Tarefa repetida!")
                return redirect('index')
            else:
                tarefa = form.save(commit=False)
                categoria = Categoria.objects.get(pk = request.POST['categoria'] )
                tarefa.categoria = categoria
                tarefa.save()
                messages.success(request,"Tarefa cadastrada")
                return redirect('index')

    #else:
        #form = QuadroForm()
    categorias = Categoria.objects.all()
    return render(request,'taskProject/criar_tarefa.html',{'categorias':categorias})   



def listar_tarefas(request,id):
    #quadros = Quadro.objects.all()
    return render(request, 'taskProject/listar_tarefas.html')