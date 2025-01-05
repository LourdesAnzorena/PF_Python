from django.contrib import admin
from PFApp.models import  Usuario,Plan,Pago,Avatar, Suscripcion

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["usuario","estado_suscripcion" ]
    ordering= ("usuario","estado_suscripcion")
    search_fields= ("usuario","estado_suscripcion")
        
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    ordering= ("nombre", )
    search_fields= ( "nombre", )
    
@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ["id", "metodo_pago" ]
    ordering= ("id", "metodo_pago" )
    search_fields= ( "metodo_pago", )


@admin.register(Avatar)
class AvatarAdmin(admin.ModelAdmin):
    list_display = ('user', 'imagen')

@admin.register(Suscripcion)
class SuscripcionAdmin(admin.ModelAdmin):
        list_display = ["usuario", "plan","activa" ]
        ordering= ("fecha_inicio",  )
        search_fields= ( "usuario","plan" )

        
