from django.shortcuts import render
from .forms import AlunoForm
from django.contrib import  messages
from trab2web.models import Aluno
# Create your views here.

def index(request):
    alunos = Aluno.objects.all()

    testChave = {

         'alunos': alunos

    }
    return render(request, 'index.html', testChave)

def index(request):
    return render(request, 'index.html')

def aluno(request):
    form = AlunoForm(request.POST or None)
    if str(request.method) == 'POST':

      if form.is_valid():
         messages.success(request, 'Cadastro realizado  com sucesso')
         form =AlunoForm()



    else:

        messages.error(request, 'Erro cadastrar')

    context = {

        'form': form

    }

    return render(request, 'index.html', context)