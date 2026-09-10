from persistent import Persistent

class Categoria(Persistent):

    def __init__(self, idCategoria, nombre):
        self.idCategoria = idCategoria
        self.nombre = nombre
        self.productos = []

    def agregarProducto(self, producto):
        self.productos.append(producto)

    def eliminarProducto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)

    def consultarProductos(self):
        return self.productos