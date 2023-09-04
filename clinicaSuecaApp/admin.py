from django.contrib import admin
from clinicaSuecaApp import models

admin.register(models.Persona)
admin.register(models.Paciente)
admin.register(models.Doctor)
admin.register(models.HoraMedica)