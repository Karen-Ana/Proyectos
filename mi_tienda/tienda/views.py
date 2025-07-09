from django.shortcuts import render
from .models import Producto

def inicio(request):
    return render(request, 'inicio.html')

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto.html', {'productos': productos})
