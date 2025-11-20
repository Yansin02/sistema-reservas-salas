from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['rut_persona', 'nombre_completo', 'email', 'telefono']
        widgets = {
            'rut_persona': forms.TextInput(attrs={
                'placeholder': '12.345.678-9',
                'pattern': '^\\d{1,2}\\.\\d{3}\\.\\d{3}-[0-9kK]{1}$'
            }),
            'nombre_completo': forms.TextInput(attrs={'placeholder': 'Nombre Apellido'}),
            'email': forms.EmailInput(attrs={'placeholder': 'correo@ejemplo.com'}),
            'telefono': forms.TextInput(attrs={'placeholder': '+56 9 1234 5678'}),
        }
        labels = {
            'rut_persona': 'RUT',
            'nombre_completo': 'Nombre Completo',
        }