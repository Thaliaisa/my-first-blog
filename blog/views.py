from django.shortcuts import render #função render recebe um request (requisição do navegador) pega o Html, monta a página e devolve para o usuário
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request): #função post_list criada/ request: objeto enviado pelo navegador (quem está acessando, qual página, dados enviados)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html', {'posts': posts}) #retorna o valor que obtém ao chamar outra função reder, que irá renderizar (montar) nosso modelo blog/post_list/html .
#devolva essa resposta ao navegador / blog... é o caminho que será carregado
