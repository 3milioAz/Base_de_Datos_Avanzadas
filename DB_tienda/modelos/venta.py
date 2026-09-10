from persistent import Persistent
from datetime import datetime

class Venta(Persistent):

    def __init__(self, idVenta, cliente):
        self.idVenta = idVenta
        self.fecha = datetime.now()
        self.cliente = cliente
        self.productos = []
        self.total = 0

    def agregarProducto(self, producto, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
            return

        if cantidad > producto.existencias:
            print("No hay existencias suficientes.")
            return

        self.productos.append({
            "producto": producto,
            "cantidad": cantidad,
            "precio": producto.precio
        })

    def calcularTotal(self):
        self.total = sum(
            item["cantidad"] * item["precio"]
            for item in self.productos
        )
        return self.total

    def consultarProductos(self):
        return self.productos

    def registrarVenta(self):
        for item in self.productos:
            item["producto"].disminuirExistencias(item["cantidad"])

        self.calcularTotal()