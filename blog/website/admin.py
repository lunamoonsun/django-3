from django.contrib import admin
from .models import Post # Importa o modelo Post que foi criado no arquivo models.py

# Register your models here.
# Registra os models para que eles apareçam no painel de administração do django

admin.site.register(Post) # Registra o modelo Post para que ele apareça no painel de administração do django
                            # A partir disso pode criar um novo post no painel de administração do django
                        # E será gravado no banco de dados