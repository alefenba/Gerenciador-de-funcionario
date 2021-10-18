from django import forms
from helloworld.models import Funcionario

class InsereFuncionarioForm(forms.ModelForm):

    class Meta:
        model = Funcionario
        fields= [
            'nome',
            'sobrenome',
            'cpf',
            'remuneracao'
        ]

        exclude = ['tempo_de_servico']
        