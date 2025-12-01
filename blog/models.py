from django.conf import settings # são linhas que adicionam trechos de outros arquivos, assim não precisa copiar e colar / importar as configurações do Django (settings.py)
from django.db import models # importa as classes de modelos (Model, Charfiel, etc)
from django.utils import timezone #importa as funções relacionadas ao tempo (timezone.now)

#cria uma classe chamada Post que representa um modelo/tabela no bancdo de dados 
class Post(models.Model): # define o nosso modelo é um object / class é a palavra chave para definir objetos / Post é o nome do modelo / models.Model significa que é um modelo do Django
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # models.ForeignKey é um link para outro modelo / ForeignKey = relação de muitos-para-um
    title = models.CharField(max_length=200) # models.Charfield é assim que defini um texto com número limitados de caracteres
    text = models.TextField() # models.TextField é para textos longos, sem limite
    created_date = models.DateTimeField(default = timezone.now) # models.DateTimeField é para data e hora 
    published_date = models.DateTimeField(blank=True, null=True)

# método responsável por "publicar" o post 
    def publish(self): #def significa que se trata de uma função/método published é o nome do método
        self.published_date = timezone.now() # define a data de publicação como o momento atual
        self.save() #salva o objeto no banco de dados
# Define a representação textual do objeto (como ele aparece no admin)
    def __str__(self): 
        return self.title #exibe o título do post como nojme 
