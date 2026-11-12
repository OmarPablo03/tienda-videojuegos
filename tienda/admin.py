from django.contrib import admin
from .models import Videojuego

@admin.register(Videojuego)
class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'plataforma', 'genero', 'precio', 'stock')
    search_fields = ('titulo', 'plataforma', 'genero')
    list_filter = ('plataforma', 'genero')