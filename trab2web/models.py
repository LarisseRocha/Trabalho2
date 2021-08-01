from django.db import models

# Create your models here.
class Aluno(models.Model):

    nome = models.CharField('Nome do aluno:', max_length=100)
    ingresso = models.DateField('Ingresso', max_length=100)
    nota = models.IntegerField('Nota do aluno:')

    def __str__(self):
        return self.nome