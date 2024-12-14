from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'password', 'fecha_nacimiento', 'direccion', 'telefono']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo Electrónico',
            'password': 'Contraseña',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
        }
