from django.db import models
from django.utils import timezone
from datetime import timedelta

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
    
    rut_persona = models.CharField(max_length=12, verbose_name="RUT")
    nombre_completo = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15, blank=True)
    fecha_hora_inicio = models.DateTimeField(auto_now_add=True)
    fecha_hora_termino = models.DateTimeField()
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    
    def save(self, *args, **kwargs):
        # Calcular fecha_hora_termino como fecha_hora_inicio + 2 horas
        if not self.fecha_hora_termino and self.fecha_hora_inicio:
            self.fecha_hora_termino = self.fecha_hora_inicio + timedelta(hours=2)
        elif not self.fecha_hora_termino:
            self.fecha_hora_termino = timezone.now() + timedelta(hours=2)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Reserva {self.id} - {self.sala.nombre} - {self.rut_persona}"
    
    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"