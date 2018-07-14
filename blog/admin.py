from django.contrib import admin
from .models import Post # importamos (incluimos) el modelo Post

admin.site.register(Post) #Registramos el modelo para hacerlo visible