from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import CrearForm
from .models import Ciius

@login_required
def Listar_Ciiu(request):
    # Lista = Ciiu.objects.filter(user=request.user, date)
    Listas = Ciius.objects.all()
    return render(request, 'Listar_Ciiu.html', {'Listas': Listas})

@login_required
def Listar_Ciiu(request):
    # Lista = Ciiu.objects.filter(user=request.user, date)
    Listas = Ciius.objects.all()
    return render(request, 'Listar_Ciiu.html', {'Listas': Listas})

@login_required
def Crear_Ciiu(request):
    if request.method == 'GET':
        return render(request, 'Crear_Ciiu.html', {
        'form': CrearForm
        })
    else:
        try:
            form = CrearForm(request.POST)
            new = form.save(commit = False)
            # new.user = request.user
            new.save()
            return render(request, 'Crear_Ciiu.html', {
            'form': CrearForm
            })
        except ValueError:
            return render(request, 'Crear_Ciiu.html', {
            'form': CrearForm,
            'error':'Ingrese valores válidos'
            })

@login_required        
def Ciiu_Creada(request, Ciius_id):
    if request.method == 'GET':
        Actividades = get_object_or_404(Ciius, pk=Ciius_id)
        form = CrearForm(instance=Actividades)
        return render(request,'Ciiu_Creada.html',{'Actividades': Actividades, 'form':form })
    else:
        try:
            actividad = get_object_or_404(Ciius, pk=Ciius_id)
            form = CrearForm(request.POST, instance = actividad)
            form.save()
            return redirect('Listar_Ciiu')
        except ValueError:
            return render(request,'Ciiu_Creada.html',{'Actividades': actividad, 'form':form, 'error': 'Error al actualizar'})

@login_required        
def Elimina_Ciiu(request, Ciius_id):
    Actividad = get_object_or_404(Ciius, pk=Ciius_id)
    if request.method == 'POST':
        Actividad.delete()
        return redirect('Listar_Ciiu')