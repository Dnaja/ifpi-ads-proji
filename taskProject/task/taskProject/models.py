from django.db import models


class Quadro(models.Model):

    nome = models.CharField(max_length=30, null=False)
    descricao = models.CharField(max_length=200, null=True , blank=True)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):

    nome = models.CharField(max_length=30, null=False)
    descricao = models.CharField(max_length=200, null=True , blank=True)
    data_previsao_termino = models.DateField(null = True, blank= True)
    horario_previsao_termino = models.TimeField(null = True, blank= True)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,choices=list(Categoria.objects.values_list('id','nome')))
    concluida = models.CharField(max_length = 1,null = True,blank=True)
    data_conclusao = models.DateField(null = True)
    quadro = models.ForeignKey(Quadro,on_delete=models.CASCADE,related_name="tarefas", null = False)
    status = models.CharField(max_length=1,null = False, default='1',choices = [('1','Pendente'),('2', 'Em Andamento'),('3','Concluída')])

    def __str__(self):
        return self.nome 


