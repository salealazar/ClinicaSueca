from django.contrib import admin
from clinicaSuecaApp import models

admin.site.register(models.Persona)
admin.site.register(models.Paciente)
admin.site.register(models.Doctor)
admin.site.register(models.HoraMedica)