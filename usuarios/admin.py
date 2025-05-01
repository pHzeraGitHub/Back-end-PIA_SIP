from django.contrib import admin
from .models import Usuario

# Registrando o modelo de Usuario no admin
admin.site.register(Usuario)
