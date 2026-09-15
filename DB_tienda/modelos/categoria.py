from persistent import Persistent


class Categoria(Persistent):
    """Representa una categoría de productos."""

    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        """Agrega un producto a la categoría."""
        if producto not in self.productos:
            self.productos.append(producto)

    def eliminar_producto(self, producto):
        """Elimina un producto de la categoría."""
        if producto in self.productos:
            self.productos.remove(producto)

    def consultar_productos(self):
        """Devuelve los productos de la categoría."""
        return self.productos