
from django.urls import path
from PFApp import views

urlpatterns = [
    path('inicio/', views.inicio, name= "Inicio"),
    path('planes/', views.lista_planes,name= "Planes"),
    path('registrarse/', views.registro_usuario,name="Registrarse"),
    path('perfil/', views.perfil,name= "Perfil"),
    path('cambio contraseña/', views.cambio_password),
    path('pago/', views.comprobante_pago),
    path('contactanos/',views.contactanos, name= "Contactanos"),
]
