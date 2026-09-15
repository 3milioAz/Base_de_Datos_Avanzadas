from modelos.venta import Venta


def registrar_venta(
    ventas,
    clientes,
    bitacora,
    id_venta,
    id_cliente
):
    """Crea y registra una nueva venta."""
    if id_venta in ventas:
        raise ValueError("Ya existe una venta con ese identificador.")

    cliente = clientes.get(id_cliente)

    if cliente is None:
        raise ValueError("El cliente no existe.")

    venta = Venta(id_venta, cliente)

    ventas[id_venta] = venta
    cliente.registrar_compra(venta)
    bitacora.registrar_operacion(venta)

    return venta


def agregar_producto_a_venta(venta, producto, cantidad):
    """Agrega un producto a una venta."""
    venta.agregar_producto(producto, cantidad)


def finalizar_venta(venta):
    """Registra la venta y calcula su total."""
    venta.registrar_venta()
    return venta.calcular_total()