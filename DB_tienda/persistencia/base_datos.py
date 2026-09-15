import os

import transaction
import ZODB
import ZODB.FileStorage


class BaseDatos:
    """Administra la conexión y persistencia de la base de datos ZODB."""

    def __init__(self):
        carpeta_datos = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "datos"
        )

        os.makedirs(carpeta_datos, exist_ok=True)

        archivo_base_datos = os.path.join(
            carpeta_datos,
            "tienda.fs"
        )

        self.storage = ZODB.FileStorage.FileStorage(archivo_base_datos)
        self.db = ZODB.DB(self.storage)
        self.conexion = self.db.open()
        self.raiz = self.conexion.root()

    def guardar(self):
        """Confirma los cambios realizados en la base de datos."""
        transaction.commit()

    def cerrar(self):
        """Cierra la conexión y el almacenamiento de ZODB."""
        self.conexion.close()
        self.db.close()
        self.storage.close()