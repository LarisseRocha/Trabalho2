from django.shortcuts import render
from .forms import AlunoForm
from django.contrib import messages
from trab2web.models import Aluno
# Create your views here.

def index(request):

    testChave = {
         'alunos': Aluno.objects.all()

    }
    return render(request, 'index.html', testChave)


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

def aluno(request, id):
    aluno = Aluno.objects.get(id=id)
    context = {

        'aluno': aluno

    }
    return render(request, 'aluno.html', context)


