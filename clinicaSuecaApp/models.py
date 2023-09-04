from django.db import models
from django.contrib.auth.models import AbstractUser

class Persona(AbstractUser):
    rut = models.IntegerField(primary_key=True)

class Doctor(models.Model):
    especialidad = models.CharField(max_length=100)
    persona = models.OneToOneField(Persona)

class Paciente(models.Model):
    persona = models.OneToOneField(Persona)

class HoraMedica(models.Model):
    paciente = models.ForeignKey(Paciente)
    doctor = models.ForeignKey(Doctor)
    inicio = models.DateTimeField()
    termino = models.DateTimeField()
    sucursal = models.CharField(max_length=100)
    
