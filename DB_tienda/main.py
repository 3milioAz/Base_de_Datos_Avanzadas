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


# -------------- Inicializacion de colecciones y datos iniciales --------------
def cargar_datos(): # Aqui creamos las colecciones que pertenecen a cada una de las clases

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
    proveedor1 = Proveedor("PR01", "Distribuidora MX", "2281111111", "ventas@distribuidoramx.com")
    proveedor2 = Proveedor("PR02", "Comercializadora del Centro", "2282222222", "contacto@comercializadoracentro.com")

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
    cliente1 = Cliente("CL01", "Juan Pérez", "2283333333", "juan@gmail.com")
    cliente2 = Cliente("CL02", "María López", "2284444444", "maria@gmail.com")
    cliente3 = Cliente("CL03", "Carlos Hernández", "2285555555", "carlos@gmail.com")

    raiz.clientes["CL01"] = cliente1
    raiz.clientes["CL02"] = cliente2
    raiz.clientes["CL03"] = cliente3


if not hasattr(raiz, "datos_cargados"): # Eso pregunta a la raiz primero si no existe algo en la raiz llamado categorías entonces la crea, esto para que si en algun momento volvamos a ejecutarla no se haga una nueva y borre la anterior, sino no haga nada
    cargar_datos()
    raiz.datos_cargados = True
    base.guardar()


# ------------------- Cerrar la base de datos -------------------
base.cerrar()


# ------------------- Volver a abrir la base de datos -------------------
base = BaseDatos()
raiz = base.raiz

# ------------------- Operaciones de negocio -------------------

# Registrar una venta
venta = Venta("V001", raiz.clientes["CL01"])

venta.agregarProducto(raiz.productos["P001"], 2)
venta.agregarProducto(raiz.productos["P002"], 3)

venta.registrarVenta()
raiz.ventas["V001"] = venta
raiz.clientes["CL01"].registrarCompra(venta)
raiz.bitacora.registrarOperacion(venta)


# Registrar entrada de mercancía
entrada = EntradaMercancia("E001", raiz.proveedores["PR01"])

entrada.agregarProducto(raiz.productos["P001"], 10)
entrada.registrarEntrada()

raiz.entradas["E001"] = entrada
raiz.bitacora.registrarOperacion(entrada)


base.guardar()

print("\nOperaciones realizadas correctamente.")
print("Total de la venta V001:", venta.total)


# ------------------- Consultas -------------------

print("\n--- 1. Todos los productos ---")

for producto in raiz.productos.values():
    print(producto.codigoProducto, "-", producto.nombre, "-", producto.precio)


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


# ------------------- Cerrar la base de datos -------------------
base.cerrar()