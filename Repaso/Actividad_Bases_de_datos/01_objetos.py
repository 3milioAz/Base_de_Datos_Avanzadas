class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def mostrar_informacion(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año: {self.anio}")




# NO MODIFICAR
libro1 = Libro(
    "Cien años de soledad",
    "Gabriel García Márquez",
    1967
)

libro2 = Libro(
    "El principito",
    "Antoine de Saint-Exupéry",
    1943
)

# COMPLETAR:

libro3 = Libro(
    "Crepusculo",
    "Stephenie Meyer",
    2005
)


print("------- Libro 1 -------")
libro1.mostrar_informacion()

print("\n------- Libro 2 -------")
libro2.mostrar_informacion()

print("\n------- Libro 3 -------")
libro3.mostrar_informacion()


# --------------- Explicar ---------------

'''
Estado: Es la informacion actual del objeto. En este caso: del libro_1
- Titulo: "Cien años de soledad"
- Autor: "Gabriel García Márquez"
- Anio: 1967

Propiedades: Son los atributos del objeto:
    self.titulo = titulo
    self.autor = autor
    self.anio = anio
    
Comportamientos: Son las acciones que el objeto puede realizar:
- mostrar_informacion()

'''