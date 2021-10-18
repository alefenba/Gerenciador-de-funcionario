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
    path('/lista', FuncionarioListView.as_view(template_name="lista.html")),
    path('/criar', FuncionarioCreateView.as_view(template_name="criar.html")),
    path('/editar', FuncionarioUpdateView.as_view(template_name="editar.html")),
    path('/excluir', FuncionarioDeleteView.as_view(template_name="excluir.html")),
    path('admin/', admin.site.urls)
]
