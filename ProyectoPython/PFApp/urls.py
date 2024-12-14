
from django.urls import path
from PFApp import views

urlpatterns = [
    path('inicio/', views.inicio, name= "Inicio"),
    path('planes/', views.lista_planes,name= "Planes"),
    path('registrarse/', views.registro_usuario,name="Registrarse"),
    path('perfil/', views.perfil,name= "Perfil"),
    path('pago/', views.comprobante_pago, name='comprobante_pago'),
    path('agregar-pago/', views.agregar_pago, name="agregar_pago"),
    path('contactanos/',views.contactanos, name= "Contactanos"),
]
