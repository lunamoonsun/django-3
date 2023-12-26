from django.contrib import admin
from .models import Post # Importa o modelo Post que foi criado no arquivo models.py

# Register your models here.
# Registra os models para que eles apareçam no painel de administração do django

# admin.site.register(Post) # Registra o modelo Post para que ele apareça no painel de administração do django
                            # A partir disso pode criar um novo post no painel de administração do django
                        # E será gravado no banco de dados

class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'sub_title', 
        'full_name', 'categories', 
        'deleted'] # Aqui indica que, (deseja que mostre o título e o sub_título)
    
    search_fields = ['title', 'sub_title'] # Aqui indica um campo de pesquisa para aquela página 
    # fields = ('title', 'sub_title')


    def get_queryset(self, request):
        return Post.objects.filter(deleted=False) # Aqui indica que, (deseja que mostre apenas os que não estão deletados 

admin.site.register(Post, PostAdmin) # Aqui indica que, (deseja que poste o post, igual a classe definida por PostAdmin)