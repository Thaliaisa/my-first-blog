"""uma view é uma função em py que receve uma requisição e retorna uma resposta
Quando um usuário acessa uma URL, O django executa uma view, que decide o que mostrar na tela"""

from django.urls import path 
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), #o path mapeia uma URL para uma view 
]