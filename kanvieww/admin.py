from django.contrib import admin

from .models import *

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nombre","fecha_nacimiento","documento","celular","direccion","edad"]
    
    search_fields = ["documento","nombre"]


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ["documento", "nombre", "cargo", "celular", "direccion", "salario", "edad", "fecha_nacimiento", "tareas_realizadas"]
    search_fields = ["documento", "nombre"]


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "categoria", "cantidad", "precio", "codigo_producto"]
    search_fields = ["nombre", "categoria", "codigo_producto"]


@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ["nombre", "celular", "documento"]
    search_fields = ["nombre", "documento"]


@admin.register(AnalisisFinanciero)
class AnalisisFinancieroAdmin(admin.ModelAdmin):
    list_display = ["gastos", "fuentes_ingresos", "productos_vendidos", "id_administrador"]
    search_fields = ["id_administrador__nombre", "id_administrador__documento"]


@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ["cantidad", "id_producto"]
    search_fields = ["id_producto__nombre", "id_producto__codigo_producto"]


@admin.register(Catalogo)
class CatalogoAdmin(admin.ModelAdmin):
    list_display = ["categorias", "id_inventario", "id_producto"]
    search_fields = ["categorias", "id_producto__nombre", "id_producto__codigo_producto"]


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ["codigo_pedido", "fecha_creacion", "hora_creacion", "estado", "id_cliente", "id_empleado", "id_producto"]
    search_fields = ["codigo_pedido", "estado", "id_cliente__nombre", "id_cliente__documento"]


@admin.register(TareasPedido)
class TareasPedidoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "fecha_inicio", "fecha_fin", "estado", "id_pedido"]
    search_fields = ["nombre", "estado", "id_pedido__codigo_pedido"]


@admin.register(Actividades)
class ActividadesAdmin(admin.ModelAdmin):
    list_display = ["nombre", "fecha_inicio", "fecha_fin", "estado", "id_tarea"]
    search_fields = ["nombre", "estado", "id_tarea__nombre"]


@admin.register(Historial)
class HistorialAdmin(admin.ModelAdmin):
    list_display = ["hora_creacion", "fecha_creacion", "id_cliente", "id_empleado", "id_producto"]
    search_fields = ["id_cliente__nombre", "id_cliente__documento", "id_empleado__nombre"]


@admin.register(Calendario)
class CalendarioAdmin(admin.ModelAdmin):
    list_display = ["fecha", "año", "mes", "nombre_mes", "dia", "nombre_dia", "id_pedido"]
    search_fields = ["nombre_mes", "nombre_dia", "id_pedido__codigo_pedido"]
