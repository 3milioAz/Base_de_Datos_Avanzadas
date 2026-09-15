from persistent import Persistent


class Bitacora(Persistent):
    """Registra las operaciones realizadas en el sistema."""

    def __init__(self):
        self.operaciones = []

    def registrar_operacion(self, operacion):
        """Registra una operación en la bitácora."""
        self.operaciones.append(operacion)

    def consultar_operaciones(self):
        """Devuelve todas las operaciones registradas."""
        return self.operaciones

    def buscar_operacion(self, id_operacion):
        """Busca una operación por su identificador."""
        for operacion in self.operaciones:
            if getattr(operacion, "id_venta", None) == id_operacion:
                return operacion

            if getattr(operacion, "id_entrada", None) == id_operacion:
                return operacion

        return None