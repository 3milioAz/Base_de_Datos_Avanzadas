def obtener_productos(productos):
    """Devuelve todos los productos registrados."""
    return list(productos.values())


def productos_disponibles(productos):
    """Devuelve los productos que tienen existencias."""
    return [
        producto
        for producto in productos.values()
        if producto.verificar_disponibilidad()
    ]


def productos_bajo_stock(productos, limite_stock):
    """Devuelve productos cuyo stock está por debajo del límite."""
    return [
        producto
        for producto in productos.values()
        if producto.existencias < limite_stock
    ]


def productos_por_precio(productos, precio_minimo):
    """Devuelve productos cuyo precio supera el valor indicado."""
    return [
        producto
        for producto in productos.values()
        if producto.precio > precio_minimo
    ]


def productos_por_proveedor(proveedor):
    """Devuelve los productos proporcionados por un proveedor."""
    return proveedor.consultar_productos()


def ventas_cliente(cliente):
    """Devuelve las ventas realizadas por un cliente."""
    return cliente.consultar_ventas()


def total_ventas(ventas):
    """Calcula el total acumulado de todas las ventas."""
    return sum(
        venta.total
        for venta in ventas.values()
    )


def total_ventas_diarias(ventas, fecha):
    """Calcula el total de ventas realizadas en una fecha."""
    return sum(
        venta.total
        for venta in ventas.values()
        if venta.fecha.date() == fecha
    )