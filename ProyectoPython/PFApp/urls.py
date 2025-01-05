
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from PFApp import views
from .views import ComprobantePagoView,AboutUsView

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('about-us/', AboutUsView.as_view(), name='about_us'),
    path('planes/',  views.planes_view, name="Planes"),
    path('registrarse/', views.registro_usuario, name="Registrarse"),
    path('perfil/', views.perfil, name="Perfil"),
    path('agregar-pago/', views.agregar_pago, name="agregar_pago"),
    path('contactanos/', views.contactanos, name="Contactanos"),
    path('agregar-plan/', views.agregar_plan, name="agregar_plan"), 
    path('planes/<int:plan_id>/actualizar/', views.actualizar_plan, name='actualizar_plan'),
    path('planes/<int:plan_id>/eliminar/', views.eliminar_plan, name='eliminar_plan'), 
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('suscribirse/<int:plan_id>/', views.suscribirse_plan, name='suscribirse_plan'),
    path('gestionar_suscripciones/', views.gestionar_suscripciones, name='gestionar_suscripciones'),
    path('cancelar_suscripcion/<int:suscripcion_id>/', views.cancelar_suscripcion, name='cancelar_suscripcion'),
    path('actualizar_avatar/', views.actualizar_avatar, name='actualizar_avatar'),
    path('comprobante_pago/', ComprobantePagoView.as_view(), name='comprobante_pago'),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    

