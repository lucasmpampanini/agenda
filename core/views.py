from django.shortcuts import render, redirect
from core.models import Eevnto
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def login_submit(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'Usuario ou senha invalido')
    return redirect('/')
        
@login_required(login_url='/login/')
def lista_eventos(request):
    user = request.user
    evento = Eevnto.objects.filter(usuario=user)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)