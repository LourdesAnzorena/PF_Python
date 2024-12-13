from django.shortcuts import render
from django.http import HttpResponseRedirect  
from django.urls import reverse  


# Create your views here.

from django.shortcuts import HttpResponse
from .models import Plan, Usuario, Pago

def inicio(request):
    return render(request, 'PFApp/inicio.html')


def lista_planes(request):
    planes = Plan.objects.all()  
    return render(request, 'PFApp/planes.html', {'planes': planes})


def registro_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        password = request.POST['password']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        
        Usuario.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            password=password,
            fecha_nacimiento=fecha_nacimiento,
            direccion=direccion,
            telefono=telefono,
            estado_suscripcion='activo'
        )
        return HttpResponseRedirect (reverse ('inicio'))  # Redirigir al inicio
    return render(request, "PFApp/registro.html")

def perfil(request, email_ingresado):
    try:
        usuario = Usuario.objects.get(email=email_ingresado)
    except Usuario.DoesNotExist:
        usuario = None
    return render(request, "PFApp/perfil.html", {'usuario': usuario})

    
def cambio_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        nuevo_password = request.POST['password']
        try:
            usuario = Usuario.objects.get(email=email)
            usuario.password = nuevo_password
            usuario.save()
            mensaje = "Contraseña actualizada correctamente."
        except Usuario.DoesNotExist:
            mensaje = "Usuario no encontrado."
        return render(request, "PFApp/cambio_contraseña.html", {'mensaje': mensaje})
    return render(request, "PFApp/cambio_contraseña.html")


def comprobante_pago(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            usuario = Usuario.objects.get(email=email)
            pagos = Pago.objects.filter(email=email).order_by('-fecha_pago')
            return render(request, "PFApp/pago.html", {'pagos': pagos, 'usuario': usuario})
        except Usuario.DoesNotExist:
            return render(request, "PFApp/pago.html", {'mensaje': "Usuario no encontrado."})
    return render(request, "PFApp/pago.html")


def contactanos(request):
    return render(request, 'PFApp/contactanos.html')