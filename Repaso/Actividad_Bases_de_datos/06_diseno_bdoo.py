from persistent import Persistent
from persistent.mapping import PersistentMapping
from persistent.list import PersistentList
from ZODB import DB
from ZODB.FileStorage import FileStorage
from datetime import datetime
import transaction


class Autor(Persistent):

    def __init__(self, nombre):
        self.nombre = nombre


class Libro(Persistent):

    def __init__(self, titulo, isbn, autor, anio):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor
        self.anio = anio
        self.disponible = True


class Usuario(Persistent):

    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula

        # COMPLETAR
        self.prestamos = PersistentList()
        # Le damos una lista que servira como historial de prestamos


class Prestamo(Persistent):

    def __init__(self, usuario, libro, fecha):
        self.usuario = usuario
        self.libro = libro

        # COMPLETAR
        self.fecha = fecha


# -------------------- Creacion de Datos --------------------
# ----------- Autores -----------

autor1 = Autor("Gabriel García Márquez")
autor2 = Autor("George Orwell")
autor3 = Autor("Antoine de Saint-Exupéry")


# ----------- Libros -----------

libro1 = Libro(
    "Cien años de soledad",
    "9780307474728",
    autor1,
    1967
)

libro2 = Libro(
    "El amor en los tiempos del cólera",
    "9780307389732",
    autor1,
    1985
)

libro3 = Libro(
    "1984",
    "9780451524935",
    autor2,
    1949
)

libro4 = Libro(
    "Rebelión en la granja",
    "9780451526342",
    autor2,
    1945
)

libro5 = Libro(
    "El principito",
    "9780156012195",
    autor3,
    1943
)


# ----------- Usuarios -----------

usuario1 = Usuario("Juan Pérez", "U001")
usuario2 = Usuario("María López", "U002")
usuario3 = Usuario("Carlos Hernández", "U003")


# ----------- Prestamos -----------

prestamo1 = Prestamo(
    usuario1,
    libro1,
    datetime.now()
)
libro1.disponible = False

prestamo2 = Prestamo(
    usuario2,
    libro2,
    datetime.now()
)
libro2.disponible = False

prestamo3 = Prestamo(
    usuario3,
    libro4,
    datetime.now()
)
libro4.disponible = False


# Relacionar los prestamos con los usuarios

usuario1.prestamos.append(prestamo1)
usuario2.prestamos.append(prestamo2)
usuario3.prestamos.append(prestamo3)


# ------------------- Colecciones -------------------

autores = PersistentMapping()   # Nos permite crear un diccionario para guardar los objetos y poder acceder a ellos mas facilmente

libros = PersistentMapping()
usuarios = PersistentMapping()
prestamos = PersistentList()
# ---------------------------
autores["A01"] = autor1
autores["A02"] = autor2
autores["A03"] = autor3
# ---------------------------
libros["L01"] = libro1
libros["L02"] = libro2
libros["L03"] = libro3
libros["L04"] = libro4
libros["L05"] = libro5
# ---------------------------
usuarios["U001"] = usuario1
usuarios["U002"] = usuario2
usuarios["U003"] = usuario3
# ---------------------------
prestamos.append(prestamo1)
prestamos.append(prestamo2)
prestamos.append(prestamo3)


# ------------------- Conexion a ZODB -------------------

storage = FileStorage("biblioteca.fs")

db = DB(storage)

connection = db.open()

root = connection.root()


# ------------------- Guardar colecciones -------------------

root.autores = autores
root.libros = libros
root.usuarios = usuarios
root.prestamos = prestamos


# Confirmar la transaccion

transaction.commit()

print("Datos almacenados correctamente en ZODB.")


# ------------------- Cerrar conexiones -------------------

connection.close()
db.close()