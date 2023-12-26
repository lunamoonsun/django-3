from django.shortcuts import render # Importa a função render que renderiza o template

def hello_blog(request):
    lista = ['Django', 'Python', 'Git', 'Html', 'Banco de Dados', 'Linux', 'Nginx', 'Uwsgi', 'Systemctl'] # Cria uma lista
    data = {'name': 'Curso de Django 3', 'lista_tecnologias': lista}
    return render(request, 'index.html', data) # Retorna o index.html que é um template que está dentro da pasta templates que está dentro da pasta website que está dentro da pasta blog