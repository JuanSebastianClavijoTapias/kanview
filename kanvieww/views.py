from django.shortcuts import render
from .models import *


def inicio(request):
    return render(request, 'index.html')

def seccion_clientes(request):
    datos = Cliente.objects.all()
    return render(request, 'pages/clientes.html', {
        "datos": datos
    })


