from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Contratista(models.Model):
    licencia = models.IntegerField(null=True, blank=True)
    nombre = models.CharField(max_length=20, null=True, blank=True, default=None)
    apellido = models.CharField(max_length=100, null=True, blank=True, default=None)
    ciudad = models.CharField(max_length=100, null=True, blank=True, default=None)
