# Ejercicio 07: Unir DataFrames en Pandas
"""
Ejercicio unir DataFrames
Objetivo
Combinar dos DataFrames utilizando diferentes métodos de unión en Pandas

Instrucciones
Tienes dos DataFrames con información de ventas y productos. El primer DataFrame ventas contiene las columnas 'id_producto', 'fecha' y 'unidades_vendidas'. El segundo DataFrame productos contiene las columnas 'id_producto', 'nombre' y 'precio'. Debes realizar las siguientes tareas:

Crea los dos DataFrames con los siguientes datos:
ventas: id_producto (A1, A2, A3, A4, A2), fecha (usar fechas consecutivas desde '2023-01-01'), unidades_vendidas (10, 5, 8, 12, 7)
productos: id_producto (A1, A2, A3, A5), nombre ('Laptop', 'Monitor', 'Teclado', 'Mouse'), precio (1200, 300, 100, 50)
Realiza una unión (merge) de tipo 'inner' entre ambos DataFrames usando la columna 'id_producto'.

Realiza una unión (merge) de tipo 'left' entre ambos DataFrames.

Realiza una unión (merge) de tipo 'outer' entre ambos DataFrames.

Crea una nueva columna 'valor_total' en el resultado de la unión 'inner' que multiplique las 'unidades_vendidas' por el 'precio'.

Muestra el resultado de cada operación.
"""
import pandas as pd
from datetime import datetime, timedelta

# Datos para el DataFrame de ventas.
id_productos_ventas = ['A1', 'A2', 'A3', 'A4', 'A2']
unidades_vendidas = [10, 5, 8, 12, 7]

# TODO: Genera cinco fechas consecutivas desde 2023-01-01 y crea ventas.
fecha_inicio = datetime(2023, 1, 1)

fechas = [
    fecha_inicio + timedelta(days=i)
    for i in range(5)
]

ventas = pd.DataFrame({
    'id_producto': id_productos_ventas,
    'fecha': fechas,
    'unidades_vendidas': unidades_vendidas
})

# Datos para el DataFrame de productos.
id_productos = ['A1', 'A2', 'A3', 'A5']
nombres = ['Laptop', 'Monitor', 'Teclado', 'Mouse']
precios = [1200, 300, 100, 50]

# TODO: Crea productos con las columnas id_producto, nombre y precio.
productos = pd.DataFrame({
    'id_producto': id_productos,
    'nombre': nombres,
    'precio': precios
})

print("DataFrame de ventas:")
print(ventas)

print("\nDataFrame de productos:")
print(productos)

# TODO: Realiza la unión inner mediante id_producto.
inner_merge = pd.merge(
    ventas,
    productos,
    on='id_producto',
    how='inner'
)

print("\nUnión INNER:")
print(inner_merge)

# TODO: Realiza la unión left mediante id_producto.
left_merge = pd.merge(
    ventas,
    productos,
    on='id_producto',
    how='left'
)

print("\nUnión LEFT:")
print(left_merge)

# TODO: Realiza la unión outer mediante id_producto.
outer_merge = pd.merge(
    ventas,
    productos,
    on='id_producto',
    how='outer'
)

print("\nUnión OUTER:")
print(outer_merge)

# TODO: Añade valor_total a inner_merge multiplicando unidades_vendidas por precio.
inner_merge['valor_total'] = (
    inner_merge['unidades_vendidas'] * inner_merge['precio']
)

print("\nUnión INNER con columna valor_total:")
print(inner_merge)

