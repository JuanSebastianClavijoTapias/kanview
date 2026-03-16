from django.urls import path
from . import views

urlpatterns = [
	path('', views.inicio, name='inicio'),
	path('clientes/', views.seccion_clientes, name='clientes'),
	path('empleados/', views.seccion_empleados, name='empleados'),
	path('pedidos/', views.seccion_pedidos, name='pedidos'),
	path('calendario/', views.seccion_calendario, name='calendario'),
	path('historiales/', views.seccion_historiales, name='historiales'),
	path('tareas/', views.seccion_tareas, name='tareas'),
	path('actividades/', views.seccion_actividades, name='actividades'),
	path('inventario/', views.seccion_inventario, name='inventario'),
	path('productos/', views.seccion_productos, name='productos'),
	path('catalogo/', views.seccion_catalogo, name='catalogo'),
	path('analisis-financiero/', views.seccion_analisis_financiero, name='analisis_financiero'),
	path('administrador/', views.seccion_administrador, name='administrador'),
]
