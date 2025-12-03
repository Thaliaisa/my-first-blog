from django.shortcuts import render #função render recebe um request (requisição do navegador) pega o Html, monta a página e devolve para o usuário

# Create your views here.

def post_list(request): #função post_list criada/ request: objeto enviado pelo navegador (quem está acessando, qual página, dados enviados)
    return render(request,'blog/post_list.html', {}) #retorna o valor que obtém ao chamar outra função reder, que irá renderizar (montar) nosso modelo blog/post_list/html .

#devolva essa resposta ao navegador / blog... é o caminho que será carregado
