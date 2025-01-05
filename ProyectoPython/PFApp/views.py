from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse,reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import update_session_auth_hash
from django.views.generic import ListView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PlanForm, UsuarioForm, RegistroForm,BusquedaPlanesForm,PagoForm,ContraseñaForm, SuscripcionForm,AvatarForm
from .models import Plan, Usuario, Pago, Suscripcion,Avatar


def inicio(request):
    return render(request, 'PFApp/inicio.html')

class AboutUsView(TemplateView):
    template_name = "PFApp/about_us.html"

@login_required
def agregar_plan(request):
    if not request.user.is_staff:  # Solo accesible para administradores
        return redirect('Inicio')

    if request.method == "POST":
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Plan agregado con éxito.')
            return redirect('Planes')
    else:
        form = PlanForm()

    return render(request, 'PFApp/agregar_plan.html', {'form': form})


def registro_usuario(request):
    if request.method == 'POST':
        registro_form = RegistroForm(request.POST)
        usuario_form = UsuarioForm(request.POST)

        if registro_form.is_valid() and usuario_form.is_valid():
           
            user = registro_form.save(commit=False)
            user.set_password(registro_form.cleaned_data['password']) 
            user.save()

            # Crear el perfil asociado (Usuario)
            perfil = usuario_form.save(commit=False)
            perfil.usuario = user
            perfil.save()

            messages.success(request, 'Usuario registrado con éxito.')
            return redirect(reverse('Inicio'))
        else:
            messages.error(request, 'Por favor, corrija los errores del formulario.')
    else:
        registro_form = RegistroForm()
        usuario_form = UsuarioForm()

    return render(request, "PFApp/registrarse.html", {'registro_form': registro_form, 'usuario_form': usuario_form})


@login_required
def perfil(request):
    try:
        usuario = Usuario.objects.get(usuario=request.user)
    except Usuario.DoesNotExist:
        usuario = None

    # Obtener las suscripciones del usuario
    suscripciones = Suscripcion.objects.filter(usuario=request.user)

    # Obtener pagos del usuario
    pagos = Pago.objects.filter(usuario=request.user).order_by('-fecha_pago')

    context = {
        'usuario': usuario,
        'suscripciones': suscripciones, 
        'pagos': pagos,
    }

    return render(request, "PFApp/perfil.html", context)


def admin_required(user):
    return user.is_staff

@user_passes_test(admin_required)
@login_required
def agregar_pago(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            pago = form.save(commit=False)
            pago.usuario = User.objects.get(pk=request.POST.get('usuario_id'))
            pago.save()
            return redirect('comprobante_pago')
    else:
        form = PagoForm()
    
    usuarios = User.objects.all()  
    return render(request, 'PFApp/agregar_pago.html', {'form': form, 'usuarios': usuarios})

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Pago

class ComprobantePagoView(LoginRequiredMixin, ListView):
    model = Pago
    template_name = "PFApp/pago.html"
    context_object_name = "pagos"
    ordering = ['-fecha_pago']  

    def get_queryset(self):
        if self.request.user.is_staff:
            # Si el usuario es administrador, mostrar todos los pagos
            return Pago.objects.all().order_by('-fecha_pago')
        else:
            # Si es un usuario regular, mostrar solo sus pagos
            return Pago.objects.filter(usuario=self.request.user).order_by('-fecha_pago')


def contactanos(request):
    return render(request, 'PFApp/contactanos.html')

@login_required
def planes_view(request):
    form = BusquedaPlanesForm(request.GET)
    planes_disponibles = Plan.objects.all()  
    planes_filtrados = None 
    suscripcion = Suscripcion.objects.filter(usuario=request.user, activa=True).first()

    # Filtrar los planes si el formulario de búsqueda tiene datos
    if form.is_valid() and form.cleaned_data.get('query'):
        query = form.cleaned_data['query']
        planes_filtrados = planes_disponibles.filter(nombre__icontains=query)

    # Si el usuario está enviando una solicitud para cambiar de plan
    if request.method == 'POST' and 'plan' in request.POST:
        plan_id = request.POST.get('plan')
        plan = get_object_or_404(Plan, id=plan_id)

        # Verificar si el usuario ya tiene una suscripción activa
        if suscripcion:
            # Cancelar la suscripción anterior si el usuario ya tiene una activa
            suscripcion.activa = False
            suscripcion.save()

        # Crear la nueva suscripción
        nueva_suscripcion = Suscripcion(usuario=request.user, plan=plan, activa=True)
        nueva_suscripcion.save()

        messages.success(request, 'Suscripción realizada con éxito.')
        return redirect('perfil') 

    return render(request, 'PFApp/planes.html', {
        'form': form,
        'planes_disponibles': planes_disponibles,
        'planes_filtrados': planes_filtrados,
        'suscripcion': suscripcion,
        'is_staff': request.user.is_staff 
    })


@login_required
@staff_member_required
def actualizar_plan(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)
    if request.method == 'POST':
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return redirect('Planes')
    else:
        form = PlanForm(instance=plan)

    return render(request, 'PFApp/actualizar_plan.html', {'form': form, 'plan': plan})

@login_required
@staff_member_required
def eliminar_plan(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)
    if request.method == 'POST':
        plan.delete()
        return redirect('Planes')

    return render(request, 'PFApp/eliminar_plan.html', {'plan': plan})

@login_required
def editar_perfil(request):
    try:
        usuario = Usuario.objects.get(usuario=request.user)
    except Usuario.DoesNotExist:
        usuario = None

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        contraseña_form = ContraseñaForm(request.user, request.POST)
        if form.is_valid():
            form.save()
        if contraseña_form.is_valid():
            contraseña_form.save()
            update_session_auth_hash(request, request.user)  
            return redirect('Perfil')  
    else:
        form = UsuarioForm(instance=usuario)
        contraseña_form = ContraseñaForm(request.user)

    return render(request, 'PFApp/editar_perfil.html', {'form': form, 'contraseña_form': contraseña_form})

@login_required
def suscribirse_plan(request, plan_id):
    # Obtener el plan que el usuario desea seleccionar
    plan = get_object_or_404(Plan, id=plan_id)

    # Verificar si el usuario ya está suscrito a este plan
    if Suscripcion.objects.filter(usuario=request.user, plan=plan, activa=True).exists():
        messages.warning(request, 'Ya estás suscrito a este plan.')
        return redirect('Perfil')  # Redirigir al perfil si ya está suscrito

    # Marcar la suscripción activa anterior como inactiva
    suscripcion_activa = Suscripcion.objects.filter(usuario=request.user, activa=True).first()
    if suscripcion_activa:
        suscripcion_activa.activa = False
        suscripcion_activa.save()

    # Crear una nueva suscripción para el usuario con el nuevo plan
    nueva_suscripcion = Suscripcion(usuario=request.user, plan=plan, activa=True)
    nueva_suscripcion.save()

    messages.success(request, 'Suscripción realizada con éxito.')
    return redirect('Perfil') 

@login_required
def gestionar_suscripciones(request):
    try:
        usuario = Usuario.objects.get(usuario=request.user)
    except Usuario.DoesNotExist:
        return redirect('Perfi.html')

    if request.method == 'POST':
        form = SuscripcionForm(request.POST)
        if form.is_valid():
            suscripcion = form.save(commit=False)
            suscripcion.usuario = usuario
            suscripcion.save()
            return redirect('Perfi.html')
    else:
        form = SuscripcionForm()

    suscripciones = Suscripcion.objects.filter(usuario=usuario)
    context = {
        'form': form,
        'suscripciones': suscripciones,
    }
    return render(request, 'gestionar_suscripciones.html', context)


@login_required
def cancelar_suscripcion(request, suscripcion_id):
    # Obtener la suscripción
    suscripcion = get_object_or_404(Suscripcion, id=suscripcion_id, usuario=request.user)

    # Cancelar la suscripción (marcar como inactiva)
    suscripcion.activa = False
    suscripcion.save()

    messages.success(request, 'Suscripción cancelada con éxito.')
    return redirect('Perfil')

@login_required
def actualizar_avatar(request):
    avatar, created = Avatar.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=avatar)
        if form.is_valid():
            form.save()
            return redirect('Perfil')  
    else:
        form = AvatarForm(instance=avatar)
    return render(request, 'actualizar_avatar.html', {'form': form})