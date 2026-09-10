import ZODB
import ZODB.FileStorage
import transaction


class BaseDatos:

    def __init__(self):
        self.storage = ZODB.FileStorage.FileStorage("datos/tienda.fs")
        self.db = ZODB.DB(self.storage)
        self.conexion = self.db.open()
        self.raiz = self.conexion.root()

    def guardar(self):
        transaction.commit()

    def cerrar(self):
        self.conexion.close()
        self.db.close()
        self.storage.close()