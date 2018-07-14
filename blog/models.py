from django.db import models
from django.utils import timezone


class Post(models.Model): #models.Model  significa que Post es un modelo de Django, 
						#así Django sabe que debe guardarlo en la base de datos.
    author = models.ForeignKey('auth.User') #ForeignKey es relacion con otro modelo
    title = models.CharField(max_length=200) #texto con un número limitado de caracteres
    text = models.TextField() #texto largo sin límite
    created_date = models.DateTimeField( #fecha y hora
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title