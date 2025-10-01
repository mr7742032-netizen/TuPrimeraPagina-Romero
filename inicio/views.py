from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Guitarras
from inicio.forms import FormularioCreacionGuitarra

def inicio(request):
    
    return render(request, 'inicio/inicio.html')

    # return HttpResponse('<h1>ESTE ES MI PRIMER VLOG</h1>')

# def crear_guitarra_v1(request, marca, modelo):

# guitarra = Guitarra(marca=marca, modelo=modelo)  
# guitarra.save()

# return render(request. 'inicio/crear_guitarra_v1.html')

def crear_guitarra_v2(request):
    
    # print(request.GET)
    # print(request.POST)
    
    if request.method == "POST":
        formulario = FormularioCreacionGuitarra(request.POST)
        if formulario.is_valid():
            marca_nueva = formulario.cleaned_data.get('marca')
            modelo_nueva = formulario.cleaned_data.get('modelo')    
            
            guitarra = Guitarras(marca=marca_nueva, modelo=modelo_nueva)  
            guitarra.save()
            
            return redirect("listado_guitarras")

    else:
        formulario = FormularioCreacionGuitarra()
    
    return render(request, 'inicio/crear_guitarra_v2.html', {'formulario': formulario})

def listado_guitarras(request):
    
    guitarras = Guitarras.objects.all()
    
    return render(request, 'inicio/listado_guitarras.html', {'listado_de_guitarras': guitarras})    