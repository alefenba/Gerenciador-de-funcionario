"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from helloworld.views import IndexTemplateView,FuncionarioListView,FuncionarioCreateView
from helloworld.views import FuncionarioUpdateView,FuncionarioDeleteView

urlpatterns = [
    
    path('', IndexTemplateView.as_view(template_name="index.html")),
    path('funcionario/cadastrar', FuncionarioCreateView.as_view(template_name="website/criar.html")),
    path('funcionario/editar', FuncionarioUpdateView.as_view(template_name="website/editar.html")),
    path('funcionario/excluir', FuncionarioDeleteView.as_view(template_name="website/excluir.html")),
    path('funcionario/lista', FuncionarioListView.as_view(template_name="website/lista.html")),
    path('admin/', admin.site.urls)
]
