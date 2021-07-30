from django.shortcuts import render
from .forms import AlunoModelForm
from django.contrib import messages
from trab2web.models import Aluno
from django.shortcuts import redirect
# Create your views here.

def index(request):

    testChave = {
         'alunos': Aluno.objects.all()

    }
    return render(request, 'index.html', testChave)


'''def aluno(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = AlunoModelForm(request.POST or None)
            if form.is_valid():
                form.save()
                messages.success(request, 'Cadastro realizado  com sucesso')
                form = AlunoModelForm()
            else:
                 messages.error(request, 'Erro cadastrar')
        else:

            form: AlunoModelForm()
            context = {

                'form': form
            }

        return render(request, 'aluno.html', context)
    else:
        return redirect('index')'''


def aluno(request, id):
    if str(request.user) != 'AnonymousUser':
        aluno = Aluno.objects.get(id=id)
        context = {

            'aluno': aluno

         }
        return render(request, 'aluno.html', context)
    else:
        return redirect('index')

