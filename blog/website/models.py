from django.db import models

# Create your models here.
# O blog pessoal tem post

class Post(models.Model):
    title = models.CharField(max_length=100) # Título do post
    sub_title = models.CharField(max_length=200) # Sobrenome do autor
    content = models.TextField() # Conteúdo do post
    

    # Toda vez que criar um modelo, tem que criar uma migração e depois aplicar a migração para o banco de dados
    # python manage.py makemigrations   
    # python manage.py migrate