from django.db import models
from django.contrib.auth.models import AbstractUser

class Persona(AbstractUser):
    pass

class Doctor(models.Model):
    especialidad = models.CharField(max_length=100)
    usuario = models.OneToOneField(Persona, on_delete=models.CASCADE)

class Paciente(models.Model):
    usuario = models.OneToOneField(Persona, on_delete=models.CASCADE)

class HoraMedica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    inicio = models.DateTimeField()
    termino = models.DateTimeField()
    sucursal = models.CharField(max_length=100)
    
