from persistent import Persistent

class Cliente(Persistent):

    def __init__(self, idCliente, nombre, telefono, correo):
        self.idCliente = idCliente
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.ventas = []

    def registrarCompra(self, venta):
        self.ventas.append(venta)

    def consultarVentas(self):
        return self.ventas

    def consultarHistorialCompras(self):
        return self.ventas