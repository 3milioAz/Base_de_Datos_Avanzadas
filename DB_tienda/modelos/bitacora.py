from persistent import Persistent

class Bitacora(Persistent):

    def __init__(self):
        self.operaciones = []

    def registrarOperacion(self, operacion):
        self.operaciones.append(operacion)

    def consultarOperaciones(self):
        return self.operaciones

    def buscarOperacion(self, idOperacion):
        for operacion in self.operaciones:
            if operacion.idVenta == idOperacion:
                return operacion

            if operacion.idEntrada == idOperacion:
                return operacion

        return None