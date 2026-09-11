from base_datos import BaseDatos

from modelos.categoria import Categoria
from modelos.producto import Producto
from modelos.proveedor import Proveedor
from modelos.cliente import Cliente
from modelos.venta import Venta
from modelos.entrada_mercancia import EntradaMercancia
from modelos.bitacora import Bitacora


# ------------------- Abrir la base de datos -------------------
base = BaseDatos()
raiz = base.raiz


# -------------- Inicialización de colecciones y datos iniciales --------------
def cargar_datos():

    raiz.categorias = {}
    raiz.productos = {}
    raiz.proveedores = {}
    raiz.clientes = {}
    raiz.ventas = {}
    raiz.entradas = {}
    raiz.bitacora = Bitacora()

    # Categorías
    abarrotes = Categoria("C01", "Abarrotes")
    bebidas = Categoria("C02", "Bebidas")
    limpieza = Categoria("C03", "Limpieza")
    higiene = Categoria("C04", "Higiene personal")
    electronica = Categoria("C05", "Electrónica")

    raiz.categorias["C01"] = abarrotes
    raiz.categorias["C02"] = bebidas
    raiz.categorias["C03"] = limpieza
    raiz.categorias["C04"] = higiene
    raiz.categorias["C05"] = electronica

    # Productos
    producto1 = Producto("P001", "Arroz", "Arroz blanco 1 kg", 25.00, 50, abarrotes)
    producto2 = Producto("P002", "Coca-Cola", "Refresco 600 ml", 18.00, 40, bebidas)
    producto3 = Producto("P003", "Jabón", "Jabón de baño", 22.00, 30, higiene)
    producto4 = Producto("P004", "Cloro", "Cloro 1 litro", 20.00, 25, limpieza)
    producto5 = Producto("P005", "Audífonos", "Audífonos inalámbricos", 350.00, 10, electronica)
    producto6 = Producto("P006", "Galletas", "Galletas de chocolate", 30.00, 35, abarrotes)

    raiz.productos["P001"] = producto1
    raiz.productos["P002"] = producto2
    raiz.productos["P003"] = producto3
    raiz.productos["P004"] = producto4
    raiz.productos["P005"] = producto5
    raiz.productos["P006"] = producto6

    # Relacionar productos con categorías
    abarrotes.agregarProducto(producto1)
    abarrotes.agregarProducto(producto6)
    bebidas.agregarProducto(producto2)
    higiene.agregarProducto(producto3)
    limpieza.agregarProducto(producto4)
    electronica.agregarProducto(producto5)

    # Proveedores
    proveedor1 = Proveedor(
        "PR01",
        "Distribuidora MX",
        "2281111111",
        "ventas@distribuidoramx.com"
    )

    proveedor2 = Proveedor(
        "PR02",
        "Comercializadora del Centro",
        "2282222222",
        "contacto@comercializadoracentro.com"
    )

    raiz.proveedores["PR01"] = proveedor1
    raiz.proveedores["PR02"] = proveedor2

    # Relacionar proveedores con productos
    proveedor1.agregarProducto(producto1)
    proveedor1.agregarProducto(producto2)
    proveedor1.agregarProducto(producto5)

    proveedor2.agregarProducto(producto3)
    proveedor2.agregarProducto(producto4)
    proveedor2.agregarProducto(producto6)

    # Clientes
    cliente1 = Cliente(
        "CL01",
        "Juan Pérez",
        "2283333333",
        "juan@gmail.com"
    )

    cliente2 = Cliente(
        "CL02",
        "María López",
        "2284444444",
        "maria@gmail.com"
    )

    cliente3 = Cliente(
        "CL03",
        "Carlos Hernández",
        "2285555555",
        "carlos@gmail.com"
    )

    raiz.clientes["CL01"] = cliente1
    raiz.clientes["CL02"] = cliente2
    raiz.clientes["CL03"] = cliente3


if not hasattr(raiz, "datos_cargados"):

    cargar_datos()

    raiz.datos_cargados = True

    base.guardar()


# ------------------- Cerrar y volver a abrir -------------------

base.cerrar()

# ---------------- Pruebas de funcionalidad ----------------------
base = BaseDatos()
raiz = base.raiz

print("\n==========================================")
print("----------- TIENDA LA ECONÓMICA ----------")
print("-------- PRUEBAS DE FUNCIONAMIENTO -------")
print("==========================================")

print("\nBase de datos reabierta correctamente.")
print("Los datos iniciales permanecen almacenados.")


# ------------------- Prueba 1: Crear producto -------------------

print("\n--- PRUEBA 1: CREAR PRODUCTO ---")

producto_prueba = Producto(
    "P007",
    "Pan",
    "Pan de caja",
    45.00,
    20,
    raiz.categorias["C01"]
)

raiz.productos["P007"] = producto_prueba

base.guardar()

print("Producto creado correctamente.")
print("Código:", producto_prueba.codigoProducto)
print("Nombre:", producto_prueba.nombre)
print("Precio:", producto_prueba.precio)
print("Existencias:", producto_prueba.existencias)


# ------------------- Prueba 2: Consultar producto -------------------

print("\n--- PRUEBA 2: CONSULTAR PRODUCTO ---")

producto = raiz.productos.get("P007")

if producto:
    print("Producto recuperado correctamente.")
    print("Código:", producto.codigoProducto)
    print("Nombre:", producto.nombre)
    print("Precio:", producto.precio)
    print("Existencias:", producto.existencias)
else:
    print("Producto no encontrado.")


# ------------------- Prueba 3: Modificar producto -------------------

print("\n--- PRUEBA 3: MODIFICAR PRODUCTO ---")

precio_anterior = producto.precio

producto.actualizarPrecio(50.00)

base.guardar()

print("Producto modificado correctamente.")
print("Precio anterior:", precio_anterior)
print("Nuevo precio:", producto.precio)


# ------------------- Prueba 4: Eliminar producto -------------------

print("\n--- PRUEBA 4: ELIMINAR PRODUCTO ---")

del raiz.productos["P007"]

base.guardar()

if "P007" not in raiz.productos:
    print("Producto eliminado correctamente.")
else:
    print("El producto todavía existe.")


# ------------------- Prueba 5 y 6: Registrar venta e inventario -------------------

print("\n--- PRUEBA 5: REGISTRAR VENTA ---")

producto_arroz = raiz.productos["P001"]
existencias_antes = producto_arroz.existencias

venta = Venta("V002", raiz.clientes["CL01"])

venta.agregarProducto(producto_arroz, 2)
venta.agregarProducto(raiz.productos["P002"], 3)

venta.registrarVenta()

raiz.ventas["V002"] = venta
raiz.clientes["CL01"].registrarCompra(venta)
raiz.bitacora.registrarOperacion(venta)

base.guardar()

print("Venta registrada correctamente.")
print("ID de venta:", venta.idVenta)
print("Cliente:", venta.cliente.nombre)
print("Total:", venta.total)


print("\n--- PRUEBA 6: ACTUALIZAR INVENTARIO ---")

existencias_despues = producto_arroz.existencias

print("Producto:", producto_arroz.nombre)
print("Existencias antes:", existencias_antes)
print("Existencias después:", existencias_despues)

if existencias_despues < existencias_antes:
    print("Inventario actualizado correctamente.")


# ------------------- Prueba 7: Venta total diaria -------------------

print("\n--- PRUEBA 7: REPORTE DE VENTA TOTAL DIARIA ---")

hoy = venta.fecha.date()

total_diario = 0

for venta_registrada in raiz.ventas.values():

    if venta_registrada.fecha.date() == hoy:
        total_diario += venta_registrada.total

print("Fecha:", hoy)
print("Total de ventas del día:", total_diario)


# ------------------- Consultas del sistema -------------------

print("\n==========================================")
print("--------- CONSULTAS DEL SISTEMA ----------")
print("==========================================")


print("\n--- 1. Todos los productos ---")

for producto in raiz.productos.values():

    print(
        producto.codigoProducto,
        "-",
        producto.nombre,
        "- $",
        producto.precio
    )


print("\n--- 2. Productos con precio mayor a $20 ---")

for producto in raiz.productos.values():

    if producto.precio > 20:
        print(producto.nombre, "-", producto.precio)


print("\n--- 3. Productos disponibles ---")

for producto in raiz.productos.values():

    if producto.verificarDisponibilidad():
        print(producto.nombre, "-", producto.existencias)


print("\n--- 4. Productos del proveedor PR01 ---")

for producto in raiz.proveedores["PR01"].consultarProductos():

    print(producto.nombre)


print("\n--- 5. Total de ventas ---")

total_ventas = sum(
    venta.total for venta in raiz.ventas.values()
)

print("Total de ventas:", total_ventas)


# ------------------- Prueba 8: Cerrar y abrir el sistema -------------------

print("\n--- PRUEBA 8: CERRAR Y ABRIR EL SISTEMA ---")

base.cerrar()

print("Base de datos cerrada correctamente.")

base = BaseDatos()
raiz = base.raiz

print("Base de datos reabierta correctamente.")


if "V002" in raiz.ventas:

    print("Venta V002 recuperada correctamente.")
    print("Total de la venta:", raiz.ventas["V002"].total)


if "P001" in raiz.productos:

    print("Producto P001 recuperado correctamente.")
    print(
        "Existencias actuales:",
        raiz.productos["P001"].existencias
    )


print("\n==========================================")
print("---------- PRUEBAS FINALIZADAS -----------")
print("==========================================")

base.cerrar()