# Super aplicação de blog

from django.contrib import admin
from django.urls import path, include # Importa a função path e include
from .views import hello_world # Importa a função hello_world de views.py

urlpatterns = [
    path('admin/', admin.site.urls), # É um caminho para o admin, é um endereço
    path('hello/', hello_world), # URL: hello/, view: hello_world que responde a URL
    path('blog/', include('website.urls')), # URL: blog/, view: website.urls
]
