from persistent import Persistent


class Cliente(Persistent):
    """Representa un cliente de la tienda."""

    def __init__(self, id_cliente, nombre, telefono, correo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.ventas = []

    def registrar_compra(self, venta):
        """Registra una venta en el historial del cliente."""
        self.ventas.append(venta)

    def consultar_ventas(self):
        """Devuelve las ventas realizadas por el cliente."""
        return self.ventas

    def consultar_historial_compras(self):
        """Devuelve el historial de compras del cliente."""
        return self.ventas