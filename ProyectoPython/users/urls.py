from django.urls import path
from users import views
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('login/', views.login_request, name="Login"),
    path('logout', LogoutView.as_view(template_name='users/logout.html'), name='Logout'),

]