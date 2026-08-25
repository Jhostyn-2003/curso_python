# Ejercicio 10: Tablas Pivotantes
"""
Ejercicio tablas pivotantes
Objetivo
Crear una tabla pivotante para analizar datos de ventas por categoría y región

Instrucciones
Utilizando Pandas, crea una tabla pivotante que analice datos de ventas por categoría de producto y región.

Primero, crea un DataFrame con los siguientes datos:

'categoría': Distribuye 30 valores entre ['Electrónica', 'Ropa', 'Hogar']
'región': Distribuye 30 valores entre ['Norte', 'Sur', 'Este', 'Oeste']
'ventas': 30 valores aleatorios entre 100 y 1000
'unidades': 30 valores aleatorios entre 1 y 20
Luego, crea una tabla pivotante que muestre:

La suma total de ventas para cada combinación de categoría y región
Incluye totales por fila y columna (usando el parámetro margins)
Reemplaza los valores NaN con ceros
Tu solución debe importar las bibliotecas necesarias, crear el DataFrame de ejemplo y generar la tabla pivotante según las especificaciones.
"""

import pandas as pd
import numpy as np

# Generador reproducible para los datos aleatorios.
rng = np.random.default_rng(seed=42)

# TODO: Genera 30 categorías, regiones, ventas y unidades según el enunciado.
categorias = rng.choice(
    ['Electrónica', 'Ropa', 'Hogar'],
    size=30
)

regiones = rng.choice(
    ['Norte', 'Sur', 'Este', 'Oeste'],
    size=30
)

ventas = rng.integers(
    100,
    1001,
    size=30
)

unidades = rng.integers(
    1,
    21,
    size=30
)

# TODO: Crea el DataFrame con las cuatro columnas anteriores.
df = pd.DataFrame({
    'categoria': categorias,
    'region': regiones,
    'ventas': ventas,
    'unidades': unidades
})

print("DataFrame original:")
print(df)

# TODO: Crea una tabla pivotante de la suma de ventas por categoría y región.
# Incluye margins, usa "Total" como nombre de los totales y sustituye NaN por 0.
tabla_pivot = pd.pivot_table(
    df,
    values='ventas',
    index='categoria',
    columns='region',
    aggfunc='sum',
    margins=True,
    margins_name='Total',
    fill_value=0
)

print("\nTabla pivotante de ventas por categoría y región:")
print(tabla_pivot)