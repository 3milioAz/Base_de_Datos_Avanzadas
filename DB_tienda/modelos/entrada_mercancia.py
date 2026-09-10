from persistent import Persistent
from datetime import datetime

class EntradaMercancia(Persistent):

    def __init__(self, idEntrada, proveedor):
        self.idEntrada = idEntrada
        self.fecha = datetime.now()
        self.proveedor = proveedor
        self.productos = []

    def agregarProducto(self, producto, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
            return

        self.productos.append({
            "producto": producto,
            "cantidad": cantidad
        })

    def registrarEntrada(self):
        for item in self.productos:
            item["producto"].incrementarExistencias(item["cantidad"])

    def consultarProductos(self):
        return self.productos