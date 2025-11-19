from django.db import models
from django.utils import timezone

class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    estado = models.CharField(max_length=20, default='disponible')
    habilitada = models.BooleanField(default=True)
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]
    
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    nombre_cliente = models.CharField(max_length=100, default="Cliente Anónimo")
    email = models.EmailField(default="cliente@ejemplo.com")
    telefono = models.CharField(max_length=15, blank=True)
    fecha_reserva = models.DateTimeField(default=timezone.now)
    horas_contratadas = models.IntegerField(default=1)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Reserva {self.id} - {self.sala.nombre}"