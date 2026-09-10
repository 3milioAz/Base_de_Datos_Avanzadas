from persistent import Persistent

class Proveedor(Persistent):

    def __init__(self, idProveedor, nombre, telefono, correo):
        self.idProveedor = idProveedor
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.productos = []

    def agregarProducto(self, producto):
        if producto not in self.productos:
            self.productos.append(producto)

    def eliminarProducto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)

    def consultarProductos(self):
        return self.productos