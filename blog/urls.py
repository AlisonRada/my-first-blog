from django.conf.urls import url
from . import views
# Aquí sólo estamos importando la función url de Django 
# y todas nuestras vistas de la aplicación blog

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
# Como puedes ver, ahora estamos asignando una vista view 
# llamada post_list a la URL ^$. Esta expresión regular 
# coincidirá con ^ (un inicio) seguido de $ (un final), 
# por lo tanto sólo una cadena vacía coincidirá.