# Ejercicio 9: Operaciones Matemáticas y Estadísticas
"""
Ejercicio operaciones matemáticas y estadísticas
Objetivo
Calcular estadísticas descriptivas básicas de un conjunto de datos usando Pandas

Instrucciones
Dado un DataFrame con información de ventas mensuales, calcula las siguientes estadísticas:

Utiliza el método describe() para obtener un resumen estadístico completo del DataFrame.
Calcula la media, mediana y desviación estándar de la columna 'ventas'.
Encuentra el valor máximo y mínimo de la columna 'unidades'.
Calcula la correlación entre las columnas 'ventas' y 'unidades'.
Para empezar, crea un DataFrame con los siguientes datos:

import pandas as pd
import numpy as np

# Datos de ventas mensuales
data = {
    'mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'ventas': [15200, 14800, 16700, 17500, 18200],
    'unidades': [120, 115, 140, 150, 160],
    'gastos': [5100, 4800, 5400, 5800, 6000]
}

# Crea el DataFrame
df_ventas = pd.DataFrame(data)
Tu código debe imprimir los resultados de cada estadística solicitada.
"""
import pandas as pd
import numpy as np

# Datos de ventas mensuales
data = {
    'mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'ventas': [15200, 14800, 16700, 17500, 18200],
    'unidades': [120, 115, 140, 150, 160],
    'gastos': [5100, 4800, 5400, 5800, 6000]
}

# Crea el DataFrame
df_ventas = pd.DataFrame(data)

# 1. Utiliza el método describe() para obtener un resumen estadístico completo del DataFrame
# TODO: Imprimir resumen estadístico completo
print("Resumen estadístico:")
print(df_ventas.describe())

# 2. Calcula la media, mediana y desviación estándar de la columna 'ventas'
# TODO: Calcular y imprimir media, mediana y desviación estándar de 'ventas'
media_ventas = df_ventas['ventas'].mean()
mediana_ventas = df_ventas['ventas'].median()
desviacion_ventas = df_ventas['ventas'].std()

print("\nEstadísticas de ventas:")
print("Media:", media_ventas)
print("Mediana:", mediana_ventas)
print("Desviación estándar:", desviacion_ventas)

# 3. Encuentra el valor máximo y mínimo de la columna 'unidades'
# TODO: Calcular y imprimir valor máximo y mínimo de 'unidades'
max_unidades = df_ventas['unidades'].max()
min_unidades = df_ventas['unidades'].min()

print("\nUnidades:")
print("Máximo:", max_unidades)
print("Mínimo:", min_unidades)

# 4. Calcula la correlación entre las columnas 'ventas' y 'unidades'
# TODO: Calcular y imprimir la correlación entre 'ventas' y 'unidades'
correlacion = df_ventas['ventas'].corr(df_ventas['unidades'])

print("\nCorrelación entre ventas y unidades:")
print(correlacion)

# También podemos mostrar la matriz de correlación completa
# TODO: Imprimir matriz de correlación completa de 'ventas', 'unidades' y 'gastos'
matriz_correlacion = df_ventas[
    ['ventas', 'unidades', 'gastos']
].corr()

print("\nMatriz de correlación:")
print(matriz_correlacion)