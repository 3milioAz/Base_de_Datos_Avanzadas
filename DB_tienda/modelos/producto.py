from persistent import Persistent

class Producto(Persistent):

    def __init__(self, codigoProducto, nombre, descripcion, precio, existencias, categoria):
        self.codigoProducto = codigoProducto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.existencias = existencias
        self.categoria = categoria

    def incrementarExistencias(self, cantidad):
        self.existencias += cantidad

    def disminuirExistencias(self, cantidad):
        if cantidad <= self.existencias:
            self.existencias -= cantidad
        else:
            print("No hay existencias suficientes.")

    def verificarDisponibilidad(self):
        return self.existencias > 0

    def actualizarPrecio(self, nuevoPrecio):
        self.precio = nuevoPrecio