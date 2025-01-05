from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

def login_request(request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contraseña)
            
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next') or request.GET.get('next', '/perfil/')
                return redirect(next_url)
            
        msg_login = "Usuario o contraseña incorrectos"
    
    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})
