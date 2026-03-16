from django.shortcuts import render
from .models import *


def inicio(request):
    return render(request, 'index.html')


def seccion_clientes(request):
    datos = Cliente.objects.all()
    return render(request, 'pages/clientes.html', {
        "datos": datos
    })


def seccion_empleados(request):
    datos = Empleado.objects.all()
    return render(request, 'pages/empleados.html', {
        "datos": datos
    })


def seccion_pedidos(request):
    datos = Pedido.objects.all()
    return render(request, 'pages/pedidos.html', {
        "datos": datos
    })


def seccion_calendario(request):
    datos = Calendario.objects.all()
    return render(request, 'pages/calendario.html', {
        "datos": datos
    })


def seccion_historiales(request):
    datos = Historial.objects.all()
    return render(request, 'pages/historiales.html', {
        "datos": datos
    })


def seccion_tareas(request):
    datos = TareasPedido.objects.all()
    return render(request, 'pages/tareas.html', {
        "datos": datos
    })


def seccion_actividades(request):
    datos = Actividades.objects.all()
    return render(request, 'pages/actividades.html', {
        "datos": datos
    })


def seccion_inventario(request):
    datos = Inventario.objects.all()
    return render(request, 'pages/inventario.html', {
        "datos": datos
    })


def seccion_productos(request):
    datos = Producto.objects.all()
    return render(request, 'pages/productos.html', {
        "datos": datos
    })


def seccion_catalogo(request):
    datos = Catalogo.objects.all()
    return render(request, 'pages/catalogo.html', {
        "datos": datos
    })


def seccion_analisis_financiero(request):
    datos = AnalisisFinanciero.objects.all()
    return render(request, 'pages/analisis_financiero.html', {
        "datos": datos
    })


def seccion_administrador(request):
    datos = Administrador.objects.all()
    return render(request, 'pages/administrador.html', {
        "datos": datos
    })


