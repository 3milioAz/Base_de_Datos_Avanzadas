from datetime import datetime

from persistent import Persistent


class EntradaMercancia(Persistent):
    """Representa una entrada de mercancía al inventario."""

    def __init__(self, id_entrada, proveedor):
        self.id_entrada = id_entrada
        self.fecha = datetime.now()
        self.proveedor = proveedor
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        """Agrega un producto a la entrada de mercancía."""
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        self.productos.append({
            "producto": producto,
            "cantidad": cantidad
        })

    def registrar_entrada(self):
        """Incrementa las existencias de los productos."""
        for item in self.productos:
            item["producto"].incrementar_existencias(
                item["cantidad"]
            )

    def consultar_productos(self):
        """Devuelve los productos de la entrada."""
        return self.productos