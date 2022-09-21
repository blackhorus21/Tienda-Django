from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class categoria(models.Model):
    nombre=models.CharField(max_length=50)
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'


    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='blog', null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    categorias=models.ManyToManyField(categoria)
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    


    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'


    def __str__(self):
        return self.titulo