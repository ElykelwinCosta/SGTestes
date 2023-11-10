from django.contrib import admin
from .models import CustomUser

# Registro do modelo CustomUser no painel de administração
admin.site.register(CustomUser)
