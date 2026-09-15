from datetime import date

from persistencia.base_datos import BaseDatos

from modelos.bitacora import Bitacora
from modelos.categoria import Categoria
from modelos.cliente import Cliente
from modelos.entrada_mercancia import EntradaMercancia
from modelos.producto import Producto
from modelos.proveedor import Proveedor

from servicios.productos import (
    registrar_producto,
    consultar_producto,
    modificar_producto,
    eliminar_producto,
)

from servicios.ventas import (
    registrar_venta,
    agregar_producto_a_venta,
    finalizar_venta,
)

from consultas.consultas import (
    obtener_productos,
    productos_disponibles,
    productos_bajo_stock,
    productos_por_precio,
    productos_por_proveedor,
    ventas_cliente,
    total_ventas,
    total_ventas_diarias,
)


LIMITE_STOCK = 5
PRECIO_CONSULTA = 20


def cargar_datos(raiz):
    """Carga los datos iniciales de la tienda."""
    raiz.categorias = {
        "C01": Categoria("C01", "Abarrotes"),
        "C02": Categoria("C02", "Bebidas"),
        "C03": Categoria("C03", "Limpieza"),
        "C04": Categoria("C04", "Higiene personal"),
        "C05": Categoria("C05", "Electrónica"),
    }

    raiz.productos = {}

    producto_1 = Producto(
        "P001", "Arroz", "Arroz blanco",
        25.00, 50, raiz.categorias["C01"]
    )

    producto_2 = Producto(
        "P002", "Coca-Cola", "Refresco",
        18.00, 40, raiz.categorias["C02"]
    )

    producto_3 = Producto(
        "P003", "Jabón", "Jabón de baño",
        22.00, 30, raiz.categorias["C04"]
    )

    producto_4 = Producto(
        "P004", "Cloro", "Cloro para limpieza",
        20.00, 25, raiz.categorias["C03"]
    )

    producto_5 = Producto(
        "P005", "Audífonos", "Audífonos inalámbricos",
        350.00, 10, raiz.categorias["C05"]
    )

    producto_6 = Producto(
        "P006", "Galletas", "Galletas de chocolate",
        30.00, 35, raiz.categorias["C01"]
    )

    productos = [
        producto_1,
        producto_2,
        producto_3,
        producto_4,
        producto_5,
        producto_6,
    ]

    for producto in productos:
        raiz.productos[producto.codigo_producto] = producto
        producto.categoria.agregar_producto(producto)

    raiz.proveedores = {
        "PR01": Proveedor(
            "PR01",
            "Distribuidora MX",
            "2281111111",
            "ventas@distribuidoramx.com"
        ),
        "PR02": Proveedor(
            "PR02",
            "Comercializadora del Centro",
            "2282222222",
            "ventas@comercializadoracentro.com"
        ),
    }

    raiz.proveedores["PR01"].agregar_producto(producto_1)
    raiz.proveedores["PR01"].agregar_producto(producto_2)
    raiz.proveedores["PR01"].agregar_producto(producto_5)

    raiz.proveedores["PR02"].agregar_producto(producto_3)
    raiz.proveedores["PR02"].agregar_producto(producto_4)
    raiz.proveedores["PR02"].agregar_producto(producto_6)

    raiz.clientes = {
        "CL01": Cliente(
            "CL01",
            "Juan Pérez",
            "2283333333",
            "juan@email.com"
        ),
        "CL02": Cliente(
            "CL02",
            "María López",
            "2284444444",
            "maria@email.com"
        ),
        "CL03": Cliente(
            "CL03",
            "Carlos Hernández",
            "2285555555",
            "carlos@email.com"
        ),
    }

    raiz.ventas = {}
    raiz.entradas = {}
    raiz.bitacora = Bitacora()


def ejecutar_pruebas(raiz, base):
    """Ejecuta las pruebas principales de funcionamiento."""

    print("\n--- CREAR PRODUCTO ---")

    producto_prueba = registrar_producto(
        raiz.productos,
        "P007",
        "Pan",
        "Pan de caja",
        45.00,
        20,
        raiz.categorias["C01"]
    )

    base.guardar()

    print(
        f"Producto creado: "
        f"{producto_prueba.codigo_producto} - "
        f"{producto_prueba.nombre}"
    )


    print("\n--- CONSULTAR PRODUCTO ---")

    producto = consultar_producto(
        raiz.productos,
        "P007"
    )

    print(
        f"Producto encontrado: "
        f"{producto.nombre} - "
        f"${producto.precio}"
    )


    print("\n--- MODIFICAR PRODUCTO ---")

    modificar_producto(
        producto,
        50.00
    )

    base.guardar()

    print(
        f"Nuevo precio de {producto.nombre}: "
        f"${producto.precio}"
    )


    print("\n--- ELIMINAR PRODUCTO ---")

    eliminar_producto(
        raiz.productos,
        "P007"
    )

    base.guardar()

    print(
        "P007 eliminado:",
        consultar_producto(raiz.productos, "P007") is None
    )


    print("\n--- REGISTRAR VENTA ---")

    venta = registrar_venta(
        raiz.ventas,
        raiz.clientes,
        raiz.bitacora,
        "V002",
        "CL01"
    )

    agregar_producto_a_venta(
        venta,
        raiz.productos["P001"],
        2
    )

    agregar_producto_a_venta(
        venta,
        raiz.productos["P002"],
        3
    )

    total = finalizar_venta(venta)

    base.guardar()

    print(f"Venta registrada: {venta.id_venta}")
    print(f"Total de la venta: ${total:.2f}")


    print("\n--- ACTUALIZAR INVENTARIO ---")

    producto_arroz = raiz.productos["P001"]

    print(
        f"Existencias de arroz: "
        f"{producto_arroz.existencias}"
    )


    print("\n--- CONSULTAS ---")

    print("Total de productos:", len(obtener_productos(raiz.productos)))

    print(
        "Productos disponibles:",
        len(productos_disponibles(raiz.productos))
    )

    print(
        "Productos con precio mayor a $20:",
        len(
            productos_por_precio(
                raiz.productos,
                PRECIO_CONSULTA
            )
        )
    )

    print(
        "Productos con bajo stock:",
        len(
            productos_bajo_stock(
                raiz.productos,
                LIMITE_STOCK
            )
        )
    )

    print(
        "Productos de PR01:",
        len(
            productos_por_proveedor(
                raiz.proveedores["PR01"]
            )
        )
    )

    print(
        "Ventas de CL01:",
        len(
            ventas_cliente(
                raiz.clientes["CL01"]
            )
        )
    )

    print(
        f"Total de ventas: "
        f"${total_ventas(raiz.ventas):.2f}"
    )

    print(
        f"Total de ventas de hoy: "
        f"${total_ventas_diarias(raiz.ventas, date.today()):.2f}"
    )


def main():
    """Inicia el sistema y ejecuta las pruebas."""

    base = BaseDatos()
    raiz = base.raiz

    try:
        if not hasattr(raiz, "datos_cargados"):
            cargar_datos(raiz)
            raiz.datos_cargados = True
            base.guardar()

        ejecutar_pruebas(raiz, base)

    except ValueError as error:
        print(f"Error de validación: {error}")

    finally:
        base.cerrar()


if __name__ == "__main__":
    main()