import os
import ZODB
import ZODB.FileStorage
import transaction


class BaseDatos:

    def __init__(self):
        carpeta = os.path.join(os.path.dirname(__file__), "datos")
        os.makedirs(carpeta, exist_ok=True)

        archivo = os.path.join(carpeta, "tienda.fs")

        self.storage = ZODB.FileStorage.FileStorage(archivo)
        self.db = ZODB.DB(self.storage)
        self.conexion = self.db.open()
        self.raiz = self.conexion.root()

    def guardar(self):
        transaction.commit()

    def cerrar(self):
        self.conexion.close()
        self.db.close()
        self.storage.close()