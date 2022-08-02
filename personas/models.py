from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Persona(models.Model):
    genero = (
        ('F','Femenino'),
        ('M','Masculino'),
    )
    sexo = models.CharField(max_length=1,blank=True,choices=genero)
    cedula = models.IntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=20, null=True, blank=True, default=None)
    apellido = models.CharField(max_length=100, null=True, blank=True, default=None)

class Animal(models.Model):
    genero = (
        ('F','Femenino'),
        ('M','Masculino'),
    )
    sexo = models.CharField(max_length=1,blank=True,choices=genero)
    nombre = models.CharField(max_length=20, null=True, blank=True, default=None)
    tipo = models.CharField(max_length=20, null=True, blank=True, default=None)
    dueño = models.OneToOneField(Persona, related_name="Mascota", null=True, blank=True, on_delete=models.CASCADE)
    