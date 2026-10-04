class Libro:

    def __init__(self, titulo, autor, isbn, anio, editorial, categoria, num_pags, disponible=True):

        self.titulo = titulo
        self.autor = autor

        # COMPLETAR
        self.isbn = isbn

        # COMPLETAR
        self.anio = anio

        self.editorial = editorial
        self.categoria = categoria
        self.num_pags = num_pags

        self.disponible = disponible

        


libro = Libro(
    "1984",
    "George Orwell",
    "9780451524935",
    1949,
    "Debolsillo",
    "Sci-Fi",
    352
)


print("Título:", libro.titulo)
print("Autor:", libro.autor)

# COMPLETAR:
# Mostrar ISBN
print("ISBN:", libro.isbn)

# COMPLETAR:
# Mostrar año
print("Año:", libro.anio)

print("Editorial:", libro.editorial)
print("Categoria:", libro.categoria)
print("Num. Paginas:", libro.num_pags)

# COMPLETAR:
# Mostrar disponibilidad
print("Disponibilidad:", libro.disponible)