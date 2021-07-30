from django.urls import path
from .views import index, aluno

urlpatterns = [
   path('', index, name='index'),
   path('aluno/<int:id>', aluno, name='aluno'),


]

