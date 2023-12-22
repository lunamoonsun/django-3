from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hello World') # Retorna uma resposta para o usuário que acessar a URL que está dentro de urls.py