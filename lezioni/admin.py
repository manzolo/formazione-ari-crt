from django.contrib import admin
from .models import Lezione, Docente

# Registra il modello Docente
admin.site.register(Docente)

# Registra il modello Lezione
admin.site.register(Lezione)
