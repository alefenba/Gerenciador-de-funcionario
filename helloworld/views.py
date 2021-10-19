from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView
from helloworld.models import Funcionario
from website.forms import InsereFuncionarioForm

from helloworld.models import Funcionario

class IndexTemplateView(TemplateView):
    template_name = 'website/index.html'



class FuncionarioCreateView(CreateView):
    template_name = "website/criar.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy(
        "website:lista_funcionarios"
    )
    
class FuncionarioUpdateView(UpdateView):
    template_name = 'website/editar.html'
    model = Funcionario
    fields = [
        'nome',
        'sobrenome',
        'cpf',
        'tempo_de_servico',
        'remuneracao'
    ]

class FuncionarioDeleteView(DeleteView):
    template_name = "website/excluir.html"
    model = Funcionario
    context_objects_name = 'funcionario'
    success_url = reverse_lazy(
        "website:lista_funcionarios"
    )
    
class FuncionarioListView(ListView):
    template_name = "website/lista.html"
    model = Funcionario
    context_object_name = "funcionarios"
