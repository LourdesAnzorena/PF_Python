"""
URL configuration for ProyectoPython project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PFApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('planes/', views.lista_planes),
    path('registrarse/', views.registro_usuario),
    path('perfil/', views.perfil),
    path('cambio contraseña/', views.cambio_password),
    path('pago/', views.comprobante_pago),
]
