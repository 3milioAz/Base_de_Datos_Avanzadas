from ZODB import DB
from ZODB.FileStorage import FileStorage
import transaction

from persistent import Persistent


class Libro(Persistent):
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio


# CONEXIÓN A LA BASE DE DATOS

storage = FileStorage("biblioteca.fs")

# COMPLETAR:
db = storage

# COMPLETAR:
connection = db.open()

# COMPLETAR:
root = connection.root()


# CREAR LIBRO

libro = Libro(
    "La sombra del viento",
    "Carlos Ruiz Zafón",
    2001
)


# COMPLETAR:
# Guardar el libro dentro de root
root.libro = libro      # Esto guarda una referencia al objeto dentro del objeto raíz de la base de datos. Es decir guarda la conexion al objeto en la raiz


# COMPLETAR:
# Confirmar la transacción
transaction.commit()    # Hace permanente la modificacion gracias al persistent

print("Libro almacenado correctamente.")


# CERRAR CONEXIONES

connection.close()
db.close()