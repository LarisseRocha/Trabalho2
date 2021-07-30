from django import forms

class AlunoModelForm(forms.Form):
    nome = forms.CharField(label='nome')
    ingresso = forms.CharField(label='ingresso')
    nota = forms.DecimalField(label='nota')
