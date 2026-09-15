from datetime import datetime

from persistent import Persistent


class Venta(Persistent):
    """Representa una venta realizada en la tienda."""

    def __init__(self, id_venta, cliente):
        self.id_venta = id_venta
        self.fecha = datetime.now()
        self.cliente = cliente
        self.productos = []
        self.total = 0

    def agregar_producto(self, producto, cantidad):
        """Agrega un producto a la venta."""
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        if cantidad > producto.existencias:
            raise ValueError("No hay existencias suficientes.")

        self.productos.append({
            "producto": producto,
            "cantidad": cantidad,
            "precio": producto.precio
        })

    def calcular_total(self):
        """Calcula y devuelve el total de la venta."""
        self.total = sum(
            item["cantidad"] * item["precio"]
            for item in self.productos
        )

        return self.total

    def consultar_productos(self):
        """Devuelve los productos incluidos en la venta."""
        return self.productos

    def registrar_venta(self):
        """Actualiza el inventario y calcula el total de la venta."""
        for item in self.productos:
            item["producto"].disminuir_existencias(
                item["cantidad"]
            )

        self.calcular_total()