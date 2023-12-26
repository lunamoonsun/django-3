from django.urls import path, include # Importa a função path e include
from .views import hello_blog # Importa a função hello_blog de views.py 

urlpatterns = [
    path('', hello_blog), # É um caminho para o admin, é um endereço
]
