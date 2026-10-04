class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_informacion(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")


libro1 = Libro(
    "El principito",
    "Antoine de Saint-Exupéry"
)

libro2 = Libro(
    "El principito",
    "Antoine de Saint-Exupéry"
)


print("Libro 1:")
print(id(libro1))

print("\nLibro 2:")
print(id(libro2))


# COMPLETAR:
# Determinar si ambos objetos son el mismo objeto.

print(f"\nlibro 1 y libro 2 son iguales? {libro1 == libro2}")   # Son diferentes ya que aunque sean los mismos datos son 2 instancias distintas del objeto Libro por lo cual su ID es distinto


# COMPLETAR:
# Modificar el título de libro1.

libro1.titulo = "El Principe"

# COMPLETAR:
# Mostrar las propiedades de libro1 y libro2.

print("\nPropiedades de los libros")
print("------- Libro 1 -------")
libro1.mostrar_informacion()

print("\n------- Libro 2 -------")
libro2.mostrar_informacion()
