from persistent import Persistent
from ZODB import DB
from ZODB.FileStorage import FileStorage


# ------- Clases necesarias para reconstruir los objetos guardados -------

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



storage = FileStorage("biblioteca.fs")

# COMPLETAR
db = DB(storage)

# COMPLETAR
connection = db.open()

# COMPLETAR
root = connection.root()


# CONSULTA 1
# Mostrar todos los libros


print("\n--- LIBROS ---")

# COMPLETAR
for clave, libro in root.libros.items(): # Usamos clave ya que en el diccionario le agregamos un "L01" para tener una forma precisa para identificarlos, en caso de necesitarla
    print(clave,
        "| Título:", libro.titulo,
        "| Autor:", libro.autor.nombre, 
        "| ISBN:", libro.isbn, 
        "| Año:", libro.anio, 
        "| Disponible:", libro.disponible )


# CONSULTA 2
# Buscar un libro por título

titulo_buscar = "1984"

# COMPLETAR
for libro in root.libros.values(): 
    if libro.titulo == titulo_buscar:
        print(
            "| Título:", libro.titulo,
            "| Autor:", libro.autor.nombre, 
            "| ISBN:", libro.isbn, 
            "| Año:", libro.anio
        )

# CONSULTA 3
# Mostrar únicamente libros disponibles


print("\n--- LIBROS DISPONIBLES ---")

# COMPLETAR
for libro in root.libros.values(): 
    if libro.disponible:    # Si se pone el valor solo, python busca que sea verdadero (True)
        print(
            "| Título:", libro.titulo,
            "| Autor:", libro.autor.nombre, 
            "| ISBN:", libro.isbn
        )

# CONSULTA 4
# Buscar libros publicados después del año 2000


print("\n--- LIBROS DESPUÉS DEL AÑO 2000 ---")

# COMPLETAR
for libro in root.libros.values(): 
    if libro.anio > 2000:
        print(
            "| Título:", libro.titulo,
            "| Autor:", libro.autor.nombre, 
            "| ISBN:", libro.isbn, 
            "| Año:", libro.anio
        )


connection.close()
db.close()