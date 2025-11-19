from django.contrib import admin
from .models import Sala, Reserva

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'capacidad', 'estado', 'habilitada', 'disponible']
    list_filter = ['habilitada', 'estado', 'disponible']
    search_fields = ['nombre']

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['id', 'sala', 'nombre_cliente', 'email', 'fecha_reserva', 'estado']
    list_filter = ['sala', 'estado', 'fecha_reserva']
    search_fields = ['nombre_cliente', 'email']