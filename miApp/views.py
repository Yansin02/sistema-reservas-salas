from django.shortcuts import render, get_object_or_404, redirect
from .models import Sala, Reserva
from django.utils import timezone

def home(request):
    """
    Vista para la página principal
    """
    salas = Sala.objects.filter(disponible=True).order_by('nombre')
    context = {
        'salas': salas
    }
    return render(request, 'index.html', context)

def detalle_sala(request, sala_id):
    """
    Vista para mostrar los detalles de una sala
    """
    sala = get_object_or_404(Sala, id=sala_id)
    
    # Buscar reserva activa (confirmada y que no haya terminado)
    ahora = timezone.now()
    reserva_activa = Reserva.objects.filter(
        sala=sala, 
        estado='confirmada',
        fecha_hora_termino__gt=ahora  # Mayor que ahora
    ).first()
    
    context = {
        'sala': sala,
        'reserva_activa': reserva_activa,  # ← NUEVO
        'ahora': ahora  # ← NUEVO (para referencia)
    }
    return render(request, 'sala_detail.html', context)

def reservar_sala(request, sala_id):
    """
    Vista para mostrar el formulario de reserva
    """
    sala = get_object_or_404(Sala, id=sala_id, disponible=True)
    
    if request.method == 'POST':
        rut_persona = request.POST.get('rut')
        nombre_completo = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        
        # Crear la reserva (automáticamente en estado 'pendiente')
        reserva = Reserva.objects.create(
            sala=sala,
            rut_persona=rut_persona,
            nombre_completo=nombre_completo,
            email=email,
            telefono=telefono
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