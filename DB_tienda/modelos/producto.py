from persistent import Persistent


class Producto(Persistent):
    """Representa un producto disponible en la tienda."""

    def __init__(
        self,
        codigo_producto,
        nombre,
        descripcion,
        precio,
        existencias,
        categoria
    ):
        self.codigo_producto = codigo_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.existencias = existencias
        self.categoria = categoria

    def incrementar_existencias(self, cantidad):
        """Incrementa las existencias del producto."""
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        self.existencias += cantidad

    def disminuir_existencias(self, cantidad):
        """Disminuye las existencias del producto."""
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        if cantidad > self.existencias:
            raise ValueError("No hay existencias suficientes.")

        self.existencias -= cantidad

    def verificar_disponibilidad(self):
        """Indica si el producto tiene existencias disponibles."""
        return self.existencias > 0

    def actualizar_precio(self, nuevo_precio):
        """Actualiza el precio del producto."""
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        self.precio = nuevo_precio