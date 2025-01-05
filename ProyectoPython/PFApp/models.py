from django.db import models
from django.contrib.auth.models import User


class Plan(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    periodo_facturacion = models.CharField(max_length=50, choices=[('mensual', 'Mensual'), ('anual', 'Anual')])
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):  
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    fecha_suscripcion = models.DateTimeField(auto_now_add=True)
    estado_suscripcion = models.CharField(
        max_length=20,
        choices=[
            ('activo', 'Activo'),
            ('suspendido', 'Suspendido'),
            ('cancelado', 'Cancelado')
        ],
        default='activo'
    )

    def __str__(self):
        return f'{self.usuario.username} | {self.estado_suscripcion}'

class Suscripcion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='suscripciones')  
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_fin = models.DateField(null=True, blank=True) 
    activa = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.plan.nombre if self.plan else 'Sin Plan'}"

class Pago(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pagos")
    metodo_pago = models.CharField(
        max_length=100,
        choices=[
            ('tarjeta', 'Tarjeta de Crédito/Débito'),
            ('transferencia', 'Transferencia Bancaria'),
            ('paypal', 'PayPal')
        ]
    )
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pago {self.id} | {self.metodo_pago} | Usuario: {self.usuario.username}'

class Avatar(models.Model):
   
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank = True)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
 
    def __str__(self):
        return f"{self.user} - {self.imagen}"

