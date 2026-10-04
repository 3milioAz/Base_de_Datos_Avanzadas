class Libro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):

        # COMPLETAR
        if self.disponible == False:
            print("\nEl libro ya ha sido prestado y no esta disponible")
        else:
            self.disponible = False
            print("\nLibro prestado")

    def devolver(self):

        # COMPLETAR
        self.disponible = True
        print("\nLibro devuelto correctamente")

    def mostrar_estado(self):

        # COMPLETAR
        print(f"Libro disponible: {self.disponible}")


libro = Libro(
    "Don Quijote de la Mancha",
    "Miguel de Cervantes"
)


libro.mostrar_estado()

# COMPLETAR:
# Prestar el libro
libro.prestar()

# COMPLETAR:
# Mostrar nuevamente el estado
libro.mostrar_estado()

# COMPLETAR:
# Intentar prestar nuevamente el libro
libro.prestar()

# COMPLETAR:
# Devolver el libro
libro.devolver()
libro.mostrar_estado()