from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    documento = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    edad = models.IntegerField()
    
