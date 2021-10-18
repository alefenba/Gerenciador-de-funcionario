from django import forms
from django.forms import fields

from helloworld.models import Funcionario

class InsereFuncionarioForm(forms.Form):

    class Meta:
        model = Funcionario
        fields=[
            'nome',
            'sobrenome',
            'cpf',
            'remuneracao'
        ]

        exclude = ['tempo_de_servico']
        