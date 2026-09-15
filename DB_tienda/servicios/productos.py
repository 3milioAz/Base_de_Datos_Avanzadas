from modelos.producto import Producto


def registrar_producto(
    productos,
    codigo_producto,
    nombre,
    descripcion,
    precio,
    existencias,
    categoria
):
    """Crea y registra un nuevo producto."""
    if codigo_producto in productos:
        raise ValueError("Ya existe un producto con ese código.")

    producto = Producto(
        codigo_producto,
        nombre,
        descripcion,
        precio,
        existencias,
        categoria
    )

    productos[codigo_producto] = producto
    categoria.agregar_producto(producto)

    return producto


def consultar_producto(productos, codigo_producto):
    """Busca un producto por su código."""
    return productos.get(codigo_producto)


def modificar_producto(producto, nuevo_precio):
    """Modifica el precio de un producto."""
    producto.actualizar_precio(nuevo_precio)


def eliminar_producto(productos, codigo_producto):
    """Elimina un producto del registro."""
    if codigo_producto not in productos:
        raise ValueError("El producto no existe.")

    del productos[codigo_producto]


def actualizar_inventario(producto, cantidad):
    """Actualiza las existencias de un producto."""
    if cantidad > 0:
        producto.incrementar_existencias(cantidad)
    elif cantidad < 0:
        producto.disminuir_existencias(abs(cantidad))
    else:
        raise ValueError("La cantidad no puede ser cero.")