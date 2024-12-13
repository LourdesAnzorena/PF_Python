from django.contrib import admin
from PFApp.models import  Usuario,Plan,Pago

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["apellido", "nombre","estado_suscripcion" ]
    ordering= ("apellido", "nombre" )
    search_fields= ("apellido", "nombre","estado_suscripcion" )
        
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    ordering= ("nombre", )
    search_fields= ( "nombre", )
    
@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ["id", "metodo_pago" ]
    ordering= ("id", "metodo_pago" )
    search_fields= ( "metodo_pago", )
        
