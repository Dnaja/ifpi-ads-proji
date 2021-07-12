from django.shortcuts import render,redirect,reverse
from .forms import QuadroForm,CategoriaForm, TarefaForm
from .models import Quadro,Categoria, Tarefa
from django.contrib import messages
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views import generic
import datetime

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
            quadro = Quadro.objects.filter(pk=request.POST['quadro_id'])
            tarefas_associadas = Tarefa.objects.filter(quadro_id = request.POST['quadro_id']).count()            
            if (tarefas_associadas):
                messages.error(request,"Exclusão não permitida. Quadro possui tarefas associadas!")
            else:
                quadro.delete()
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

def cadastro_tarefa(request,quadro_id):
    if request.method == "POST":
        form = TarefaForm(request.POST)
        nome = request.POST['nome']
        buscar_repetido = Tarefa.objects.filter(nome__iexact = nome).count()
        data_pt = request.POST['data_previsao_termino'] #Pega o valor dentro do campo data_previsao_termino
        if form.is_valid():
            if buscar_repetido > 0:
                messages.warning(request,"Nome da Tarefa repetida!")
                return redirect('index')
            if data_pt != '': #verifica se a data tem ou não algo registrado
                data_pt_ano = int(data_pt[0] + data_pt[1] + data_pt[2] + data_pt[3]) * 360#pega só o ano da data
                data_pt_mes = int (data_pt[5] + data_pt[6]) * 30
                data_pt_dia = int(data_pt[8] + data_pt[9])
                quant_dias = data_pt_ano + data_pt_dia + data_pt_mes
                quant_dias_atuais = datetime.date.today().year * 360
                quant_dias_atuais += datetime.date.today().month * 30
                quant_dias_atuais += datetime.date.today().day

                if quant_dias < quant_dias_atuais: #Compara se a quantidade de dias da data é menor que a de dias atuais
                    messages.warning(request,"Data de término não pode ser menor que a atual!")                
                    return redirect('index')
                if (quant_dias - quant_dias_atuais) > 30:
                    messages.warning(request,"Data de término não pode ser superior a 30 dias!")                
                    return redirect('index')
                else:
                    tarefa = form.save(commit=False)
                    categoria = Categoria.objects.get(pk = request.POST['categoria'] )
                    quadro = Quadro.objects.get(pk = 18 )
                    tarefa.categoria = categoria
                    tarefa.quadro = quadro
                    tarefa.save()
                    messages.success(request,"Tarefa cadastrada")
                    return redirect('index')

              #### Urgente, Conseguir transformar a data em número de dias e ver a diferença entre elas  
            else:
                tarefa = form.save(commit=False)
                categoria = Categoria.objects.get(pk = request.POST['categoria'] )
                quadro = Quadro.objects.get(pk = quadro_id )
                tarefa.categoria = categoria
                tarefa.quadro = quadro
                tarefa.save()
                messages.success(request,"Tarefa cadastrada")
                return redirect('index')

    #else:
        #form = QuadroForm()
    categorias = Categoria.objects.all()
    return render(request,'taskProject/criar_tarefa.html',{'categorias':categorias})   



def listar_tarefas(request,id):
    quadro = Quadro.objects.get(id = id)
    tarefas = quadro.tarefas.all()
    tarefas_pendentes = quadro.tarefas.filter(status = "1")
    tarefas_em_andamento = quadro.tarefas.filter(status = "2")
    tarefas_concluidas = quadro.tarefas.filter(status = "3")
    categorias = Categoria.objects.all()
    return render(request, 'taskProject/listar_tarefas.html',
    {
        'tarefas_pendentes':tarefas_pendentes,
        'tarefas_em_andamento' : tarefas_em_andamento,
        'tarefas_concluidas': tarefas_concluidas,
        'categorias' : categorias,
        'quadro' : id,
    })

def visualizar_modal_form(request,id):

    tarefa = Tarefa.objects.filter(pk = id)
    
    tarefa = serializers.serialize('json', tarefa)
    data = {'tarefa' : tarefa}
    return JsonResponse(data)
    

def atualizar_tarefa(request):
    if (request.method == 'POST'):
        id = request.POST.get("id")
        tarefa = Tarefa.objects.get(pk = id)
        form = TarefaForm(request.POST,instance=tarefa)
        if (form.is_valid()):
            form = form.save(commit=False)
            categoria = Categoria.objects.get(pk = request.POST['categoria'])
            form.categoria = categoria
            quadro = tarefa.quadro
            #form.quadro = quadro
            #form.status = tarefa.status
            form.save()
            return redirect('listar_tarefas',id = quadro.pk)
        else:
            messages.success(request,"teste")
            return redirect('listar_tarefas',id = 18)

def excluir_tarefa(request):
    if request.method == "POST":
        tarefa = Tarefa.objects.get(pk=request.POST['tarefa_id'])
        if (tarefa.status == '2'):
            messages.error(request,"Nâo é possível excluir tarefas Em Andamento !")
        else:
            tarefa.delete()
            messages.success(request,"Tarefa excluída!")
        return redirect('index')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/cadastro.html'