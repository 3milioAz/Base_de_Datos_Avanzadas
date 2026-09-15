# Sistema de Gestión - Tienda La Económica

Sistema desarrollado en Python y ZODB para administrar productos,
categorías, proveedores, clientes, ventas y entradas de mercancía.

## Características

- Registro de productos.
- Consulta de productos.
- Modificación de productos.
- Eliminación de productos.
- Registro de ventas.
- Actualización de inventario.
- Consultas de productos y ventas.
- Persistencia de información mediante ZODB.

## Estructura

- `modelos/`: clases que representan los objetos del sistema.
- `persistencia/`: conexión y manejo de ZODB.
- `servicios/`: lógica de negocio.
- `consultas/`: consultas del sistema.
- `datos/`: almacenamiento local generado por ZODB.
- `main.py`: punto de entrada del programa.

## Instalación

Crear un entorno virtual e instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución

Desde la carpeta DB_tienda:
```bash
python main.py