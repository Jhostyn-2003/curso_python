# Ejercicio 5: DataFrames con Pandas
""" 
Ejercicio DataFrames
Objetivo
Crear un DataFrame de Pandas con datos de ventas y calcular estadísticas básicas

Instrucciones
Crea un DataFrame de Pandas que contenga información sobre ventas de productos. El DataFrame debe tener las siguientes columnas: 'producto', 'precio', 'unidades_vendidas' y 'fecha_venta'.

Incluye al menos 5 productos diferentes con sus respectivos datos. Las fechas de venta deben estar en formato datetime y corresponder al año actual.

Una vez creado el DataFrame, realiza las siguientes operaciones:

Añade una nueva columna llamada 'ingresos_totales' que calcule el producto entre 'precio' y 'unidades_vendidas'.
Muestra los productos ordenados de mayor a menor ingreso total.
Calcula y muestra el precio promedio de todos los productos.
Identifica y muestra el producto con más unidades vendidas.
Puedes comenzar importando las bibliotecas necesarias y creando un diccionario con los datos para construir el DataFrame.
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Crear datos para el DataFrame
productos = ['Laptop', 'Smartphone', 'Tablet', 'Auriculares', 'Monitor']
precios = [1200.50, 800.75, 350.25, 120.99, 250.50]
unidades_vendidas = [10, 25, 15, 40, 8]

# Generar fechas aleatorias para el año actual
año_actual = datetime.now().year
fechas = []
for _ in range(len(productos)):
    # TODO: Generar una fecha aleatoria dentro del año actual
    pass

# Crear el DataFrame
data = {
    'producto': productos,
    'precio': precios,
    'unidades_vendidas': unidades_vendidas,
    'fecha_venta': fechas
}

df = pd.DataFrame(data)

# 1. Añadir columna de ingresos totales
# TODO: Calcular ingresos totales
pass

print("DataFrame original con ingresos totales:")
print(df)
print("\n")

# 2. Mostrar productos ordenados de mayor a menor ingreso total
# TODO: Ordenar productos por ingresos totales
pass

print("Productos ordenados por ingresos totales (mayor a menor):")
print(df_ordenado[['producto', 'ingresos_totales']])
print("\n")

# 3. Calcular y mostrar el precio promedio de todos los productos
# TODO: Calcular precio promedio
pass

print(f"Precio promedio de todos los productos: ${precio_promedio:.2f}")
print("\n")

# 4. Identificar y mostrar el producto con más unidades vendidas
# TODO: Identificar producto con más unidades vendidas
pass

print("Producto con más unidades vendidas:")
print(f"Producto: {producto_mas_vendido['producto']}")
print(f"Unidades vendidas: {producto_mas_vendido['unidades_vendidas']}")
print(f"Precio: ${producto_mas_vendido['precio']}")
print(f"Ingresos totales: ${producto_mas_vendido['ingresos_totales']}")

"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Crear datos para el DataFrame
productos = ["Laptop", "Smartphone", "Tablet", "Auriculares", "Monitor"]
precios = [1200.50, 800.75, 350.25, 120.99, 250.50]
unidades_vendidas = [10, 25, 15, 40, 8]

# Generar fechas aleatorias para el año actual
anio_actual = datetime.now().year
fecha_inicio = datetime(anio_actual, 1, 1)
fecha_fin = datetime(anio_actual, 12, 31)

dias_del_anio = (fecha_fin - fecha_inicio).days

fechas = []

for _ in range(len(productos)):
    dias_aleatorios = np.random.randint(0, dias_del_anio + 1)
    fecha_aleatoria = fecha_inicio + timedelta(days=int(dias_aleatorios))
    fechas.append(fecha_aleatoria)

# Crear el DataFrame
data = {
    "producto": productos,
    "precio": precios,
    "unidades_vendidas": unidades_vendidas,
    "fecha_venta": fechas
}

df = pd.DataFrame(data)

# 1. Añadir columna de ingresos totales
df["ingresos_totales"] = df["precio"] * df["unidades_vendidas"]

print("DataFrame original con ingresos totales:")
print(df)
print("\n")

# 2. Mostrar productos ordenados de mayor a menor ingreso total
df_ordenado = df.sort_values(
    by="ingresos_totales",
    ascending=False
)

print("Productos ordenados por ingresos totales (mayor a menor):")
print(df_ordenado[["producto", "ingresos_totales"]])
print("\n")

# 3. Calcular y mostrar el precio promedio de todos los productos
precio_promedio = df["precio"].mean()

print(f"Precio promedio de todos los productos: ${precio_promedio:.2f}")
print("\n")

# 4. Identificar y mostrar el producto con más unidades vendidas
indice_mas_vendido = df["unidades_vendidas"].idxmax()
producto_mas_vendido = df.loc[indice_mas_vendido]

print("Producto con más unidades vendidas:")
print(f"Producto: {producto_mas_vendido['producto']}")
print(f"Unidades vendidas: {producto_mas_vendido['unidades_vendidas']}")
print(f"Precio: ${producto_mas_vendido['precio']:.2f}")
print(f"Ingresos totales: ${producto_mas_vendido['ingresos_totales']:.2f}")
