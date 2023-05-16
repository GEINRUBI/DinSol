from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.

def Inicio(request):
    return render(request, 'Inicio.html')


def Registrar_Usuario(request):
    if request.method == 'GET':
        return render(request, 'Registrar_Usuario.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                usuario = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                usuario.save()
                login(request, usuario)
                return redirect('Inicio')
            except IntegrityError:
                return render(request, 'Registrar_Usuario.html', {
                    'form': UserCreationForm,
                    'error': 'El Usuario ya existe'
                })
        return render(request, 'Registrar_Usuario.html', {
            'form': UserCreationForm,
            'error': 'Las Contraseñas no coinciden'
        })

@login_required
def Cerrar_Sesion(request):
    logout(request)
    return redirect('Inicio')


def Iniciar_Sesion(request):
    if request.method == 'GET':
        return render(request, 'Iniciar_Sesion.html', {
        'form': AuthenticationForm
        })
    else:
        usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if usuario is None:
            return render(request, 'Iniciar_Sesion.html', {
            'form': AuthenticationForm,
            'error': 'El Usuario o la contraseña es incorrecto'
        })
        else:
            login(request, usuario)
            return redirect('Inicio')    


# def DinSolAdm(request):
#     return render(request, 'DinSolAdm.html')