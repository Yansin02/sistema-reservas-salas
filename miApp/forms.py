from django import forms
from miApp.models import Reserva, Sala  # ← IMPORTA DESDE miApp
from django.utils import timezone
from datetime import timedelta
import re

class ReservaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo salas disponibles
        salas_disponibles = []
        for sala in Sala.objects.filter(habilitada=True, estado='disponible'):
            if sala.esta_disponible:
                salas_disponibles.append(sala.id)
        
        self.fields['sala'].queryset = Sala.objects.filter(
            id__in=salas_disponibles
        )
        
        # Agregar clases Bootstrap
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Reserva
        fields = ['rut_persona', 'sala']
        widgets = {
            'rut_persona': forms.TextInput(attrs={
                'placeholder': '12.345.678-9',
                'pattern': '[0-9kK.-]+',
                'title': 'Formato: 12.345.678-9'
            }),
        }
        labels = {
            'rut_persona': 'RUT de la persona que reserva',
            'sala': 'Sala a Reservar',
        }
        help_texts = {
            'rut_persona': 'Ingrese RUT en formato: 12.345.678-9',
        }
    
    def clean_rut_persona(self):
        rut = self.cleaned_data.get('rut_persona')
        if rut:
            # Validación básica de RUT
            rut_pattern = re.compile(r'^(\d{1,3}(?:\.\d{3}){2}-[\dkK])|(\d{7,8}-[\dkK])$')
            if not rut_pattern.match(rut):
                raise forms.ValidationError("Formato de RUT inválido. Use: 12.345.678-9")
        return rut
    
    def clean_sala(self):
        sala = self.cleaned_data.get('sala')
        if sala and not sala.esta_disponible:
            raise forms.ValidationError(
                "Esta sala no está disponible para reservar en este momento."
            )
        return sala