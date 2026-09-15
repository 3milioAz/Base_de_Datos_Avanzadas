from persistent import Persistent


class Proveedor(Persistent):
    """Representa un proveedor de productos."""

    def __init__(self, id_proveedor, nombre, telefono, correo):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.productos = []

    def agregar_producto(self, producto):
        """Agrega un producto al catálogo del proveedor."""
        if producto not in self.productos:
            self.productos.append(producto)

    def eliminar_producto(self, producto):
        """Elimina un producto del catálogo del proveedor."""
        if producto in self.productos:
            self.productos.remove(producto)

    def consultar_productos(self):
        """Devuelve los productos proporcionados."""
        return self.productos