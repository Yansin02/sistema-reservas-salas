from django.urls import path
from . import views

app_name = 'miApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('sala/<int:sala_id>/', views.detalle_sala, name='detalle_sala'),
    path('sala/<int:sala_id>/reservar/', views.reservar_sala, name='reservar_sala'),
    path('reserva/exitosa/', views.reserva_exitosa, name='reserva_exitosa'),
]