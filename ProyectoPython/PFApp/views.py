from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse

def lista_planes(request):
    #planes = Plan.objects.all()
    #return HttpResponse(request, 'planes/lista_planes.html', {'planes': planes})
    return HttpResponse('Vista Planes')

def registro_usuario(request):
    return HttpResponse("Vista Registro Usuario")

def perfil(request,email_ingresado):
        #email_ingresado = request.email  
        #return HttpResponse(request, 'usuarios/perfil.html', {'usuario': usuario})
    return HttpResponse('Vista Perfil')
    
def cambio_password(request):
    return HttpResponse('Vista Cambio de Clave')

def comprobante_pago(request):
    return HttpResponse('Vista Comprobante de Pago')