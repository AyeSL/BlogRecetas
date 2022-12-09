from django.db import models
from datetime import datetime as dt

# Create your models here.

class usuario(models.Model):
    nombre=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    
class categoria(models.Model):
    nombre=models.CharField(max_length=40)
    
class post(models.Model):
    titulo=models.CharField(max_length=100)
    categoria= models.CharField(max_length=40)
    usuario=models.CharField(max_length=40)
    
    # creado_el=models.DateField(default=dt.now())

class comentario(models.Model):
    nombre=models.CharField(max_length=40)
    comentario=models.CharField(max_length=100)
    email=models.EmailField(max_length=40)
    
    # creado_el=creado_el=models.DateField(default=dt.now())
    