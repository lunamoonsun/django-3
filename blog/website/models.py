from django.db import models

class Categorias(models.TextChoices):
     TECH = 'TC', 'Tecnologia'
     CR = 'CR', 'Curiosidade' 
     GR = 'GR', 'Geral'


# Create your models here
# O blog pessoal tem post
class Post(models.Model):
    title = models.CharField(max_length=100) # Título do post
    sub_title = models.CharField(max_length=200) # Sobrenome do autor
    content = models.TextField() # Conteúdo do post

    categories = models.CharField( # Define as categorias do post
        max_length=2,
        choices=Categorias.choices,
        default=Categorias.GR,
    )

    deleted = models.BooleanField(default=True) # Aprovação do post, vai ter um checkbox no painel de administração do django 

    def __str__(self):
        return self.title
    
    def full_name(self): #  Juncao do titulo e subtitulo em uma nova coluna
        return self.title + self.sub_title
    
    full_name.admin_order_field  = 'title' # Ordernação baseado no título

    # Toda vez que criar um modelo, tem que criar uma migração e depois aplicar a migração para o banco de dados
    # python manage.py makemigrations   
    # python manage.py migrate