from django.contrib import admin
from .models import Sala, Reserva

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'capacidad', 'estado', 'habilitada', 'disponible']
    list_filter = ['habilitada', 'estado', 'disponible']
    search_fields = ['nombre']

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['id', 'rut_persona', 'nombre_completo', 'sala', 'fecha_hora_inicio', 'fecha_hora_termino', 'estado']
    list_filter = ['sala', 'estado', 'fecha_hora_inicio']
    search_fields = ['rut_persona', 'nombre_completo', 'email']
    readonly_fields = ['fecha_hora_inicio', 'fecha_hora_termino']
    date_hierarchy = 'fecha_hora_inicio'