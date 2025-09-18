from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    
    return render(request, 'inicio.html')

# return HttpResponse('<h1>ESTE ES MI PRIMER VLOG</h1>')
# Create your views here.
