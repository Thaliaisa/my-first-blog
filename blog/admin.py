from django.contrib import admin #importa o sistema de administração do Django 
from .models import Post #pega a classe Post que foi criada em models.py 

admin.site.register(Post) #registra o modelo post no painel admin do Django / admin é o módulo importado na linha 1 / .site se refere ao objeto que controla do site da admin / register - adicione esse modelo ao admin

