from django.db import models

# Create your models here.

class Plan(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    periodo_facturacion = models.CharField(max_length=20, choices=[('mensual', 'Mensual'), ('anual', 'Anual')])
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    fecha_suscripcion = models.DateTimeField(auto_now_add=True)
    estado_suscripcion = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('suspendido', 'Suspendido'), ('cancelado', 'Cancelado')])
    
class Pago(models.Model):
    metodo_pago = models.CharField(max_length=50)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)