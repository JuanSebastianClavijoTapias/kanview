from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    documento = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    edad = models.IntegerField()
    
class Empleado(models.Model):
    documento = models.CharField(max_length=40)
    nombre = models.CharField(max_length=100)
    #tapiceros, costura, gerente, secretario
    cargos = (
        ("costr","Costurero"),
        ("tapcr", "Tapicero"),
        ("gerente","Gerente"),
        ("secre", "Secretario")
    )
    cargo = models.CharField(choices=cargos, max_length=10, default="tapcr")
    celular = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    salario = models.DecimalField()
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    tareas_realizadas = models.IntegerField()
    
