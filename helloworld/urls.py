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
    path('', IndexTemplateView.as_view(),name="index"),
    path('funcionario/cadastrar', FuncionarioCreateView.as_view(),name="cadastro_funcionario"),
    path('funcionario/',FuncionarioListView.as_view(),name="lista_funcionarios"),
    path('funcionario/<pk>', FuncionarioUpdateView.as_view(),name="atualiza_funcionario"),
    path('funcionario/excluir/<pk>', FuncionarioDeleteView.as_view(),name="deleta_funcionario"),
    path('admin/', admin.site.urls)
]
