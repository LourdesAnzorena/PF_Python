from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .models import Usuario, Plan, Pago,Suscripcion,Avatar


# Formulario de registro de usuario
class RegistroForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput, 
        label="Contraseña",
        help_text="Debe contener al menos 8 caracteres."
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput, 
        label="Confirmar Contraseña"
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electrónico',
            'password': 'Contraseña',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data


# Formulario para editar o agregar perfil
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['fecha_nacimiento', 'direccion', 'telefono']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
        }

# Formulario para editar contraseña
class ContraseñaForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput, label="Contraseña Actual")
    new_password1 = forms.CharField(widget=forms.PasswordInput, label="Nueva Contraseña")
    new_password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmar Nueva Contraseña")

# Formulario para agregar plan
class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['nombre', 'descripcion', 'precio', 'periodo_facturacion', 'activo'] 

# Formulario para agregar pago
class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['metodo_pago', 'monto']
        
# Formulario para busqueda de plan
class BusquedaPlanesForm(forms.Form):
    query = forms.CharField(
        required=False,
        label="Buscar planes",
        widget=forms.TextInput(attrs={'placeholder': 'Introduce el nombre del plan...'})
    )

       
# Formulario para suscribirse a plan
class SuscripcionForm(forms.ModelForm):
    class Meta:
        model = Suscripcion
        fields = ['plan']
        labels = {
            'plan': 'Selecciona un plan'
        }

#Formulario para subir imagen de Avatar
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']
