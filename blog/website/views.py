from django.shortcuts import render # Importa a função render que renderiza o template
from .models import Post # Importa o model Post que está dentro do aquivo models.py 

def hello_blog(request):
    lista = ['Django', 'Python', 'Git', 'Html', 'Banco de Dados', 'Linux', 'Nginx', 'Uwsgi', 'Systemctl'] # Cria uma lista
    list_posts = Post.objects.all() # Cria uma lista com todos os objetos do model Post, que busca os posts dentro do banco de dados

   
    data = {'name': 'Curso de Django 3', 
            'lista_tecnologias': lista, 
            'posts': list_posts
            }



    return render(request, 'index.html', data) # Retorna o index.html que é um template que está dentro da pasta templates que está dentro da pasta website que está dentro da pasta blog