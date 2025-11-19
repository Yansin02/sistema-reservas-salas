from django.shortcuts import render, get_object_or_404, redirect
from .models import Sala, Reserva
from django.utils import timezone

def home(request):
    """
    Vista para la página principal
    """
    salas = Sala.objects.filter(disponible=True)
    context = {
        'salas': salas
    }
    return render(request, 'index.html', context)

def detalle_sala(request, sala_id):
    """
    Vista para mostrar los detalles de una sala
    """
    sala = get_object_or_404(Sala, id=sala_id, disponible=True)
    context = {
        'sala': sala
    }
    return render(request, 'sala_detail.html', context)

def reservar_sala(request, sala_id):
    """
    Vista para mostrar el formulario de reserva
    """
    sala = get_object_or_404(Sala, id=sala_id, disponible=True)
    
    if request.method == 'POST':
        # Procesar el formulario de reserva
        nombre_cliente = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        fecha_reserva = request.POST.get('fecha')
        horas_contratadas = request.POST.get('horas', 1)
        
        # Crear la reserva
        reserva = Reserva.objects.create(
            sala=sala,
            nombre_cliente=nombre_cliente,
            email=email,
            telefono=telefono,
            fecha_reserva=fecha_reserva,
            horas_contratadas=horas_contratadas
        )
        
        return redirect('miApp:reserva_exitosa')
    
    context = {
        'sala': sala
    }
    return render(request, 'reservar_sala.html', context)

def reserva_exitosa(request):
    """
    Vista para mostrar confirmación de reserva
    """
    return render(request, 'reserva_exitosa.html')