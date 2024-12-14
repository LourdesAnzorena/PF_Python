from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect  
from django.urls import reverse  
from django.contrib import messages 
from .forms import UsuarioForm
import bcrypt



# Create your views here.

from django.shortcuts import HttpResponse
from .models import Plan, Usuario, Pago

def inicio(request):
    return render(request, 'PFApp/inicio.html')


def lista_planes(request):
    planes = Plan.objects.all()  
    return render(request, 'PFApp/planes.html', {'planes': planes})

def agregar_plan(request):
    if request.method == "POST" and request.user.is_staff:
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        periodo_facturacion = request.POST.get('periodo_facturacion')
        
        if nombre and descripcion and precio and periodo_facturacion:
            Plan.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                precio=precio,
                periodo_facturacion=periodo_facturacion
            )
            return redirect('Planes')
    
    return render(request, 'PFApp/agregar_plan.html')


def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False) 
            
            usuario.password = bcrypt.hashpw(usuario.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            usuario.estado_suscripcion = 'activo'
            usuario.save()  # Guarda el usuario en la base de datos
            messages.success(request, 'Usuario registrado con éxito.')
            return redirect(reverse('Inicio'))
        else:
            messages.error(request, 'Por favor, corrija los errores del formulario.')
    else:
        form = UsuarioForm()
    
    return render(request, "PFApp/registrarse.html", {'form': form})

def perfil(request):
    email_ingresado = request.GET.get('email')  
    usuario = None
    if email_ingresado:
        try:
            usuario = Usuario.objects.get(email=email_ingresado)
        except Usuario.DoesNotExist:
            usuario = None
    return render(request, "PFApp/perfil.html", {'usuario': usuario})

def comprobante_pago(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            usuario = Usuario.objects.get(email=email)
            pagos = Pago.objects.filter(usuario=usuario).order_by('-fecha_pago')
            return render(request, "PFApp/pago.html", {'pagos': pagos, 'usuario': usuario})
        except Usuario.DoesNotExist:
            return render(request, "PFApp/pago.html", {'mensaje': "Usuario no encontrado."})
    
    
    if request.user.is_authenticated and request.user.is_staff:
        pagos = Pago.objects.all().order_by('-fecha_pago')
        return render(request, "PFApp/pago.html", {'pagos': pagos})

    return render(request, "PFApp/pago.html")

def agregar_pago(request):
    if request.method == 'POST' and request.user.is_staff:
        metodo_pago = request.POST.get('metodo_pago')
        monto = request.POST.get('monto')
        
        if metodo_pago and monto:
            Pago.objects.create(
                metodo_pago=metodo_pago,
                monto=monto
            )
           
            return redirect('comprobante_pago')
    
    return render(request, 'PFApp/agregar_pago.html')

def contactanos(request):
    return render(request, 'PFApp/contactanos.html')