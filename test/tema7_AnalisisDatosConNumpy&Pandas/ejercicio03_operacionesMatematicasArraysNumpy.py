# Ejercicio 03: Operaciones Matemáticas con Arrays en Numpy
"""
Ejercicio operaciones matemáticas en arrays de Numpy
Objetivo
Cálculo de estadísticas descriptivas en arrays de NumPy

Instrucciones
Crea un array NumPy bidimensional de 4x5 con números aleatorios entre 0 y 100. Luego, realiza las siguientes operaciones:

Calcula la media de todo el array
Calcula la desviación estándar de todo el array
Encuentra el valor máximo y mínimo de todo el array
Calcula la suma de cada fila del array
Calcula la media de cada columna del array
Guarda cada resultado en variables separadas llamadas: media_total, desviacion_estandar, valor_maximo, valor_minimo, suma_filas y media_columnas.

import numpy as np

# Crear un array NumPy bidimensional de 4x5 con números aleatorios entre 0 y 100
np.random.seed(42)  # Para reproducibilidad
array = np.random.randint(0, 101, size=(4, 5))

# 1. Calcular la media de todo el array
media_total = # TODO: calcular la media del array

# 2. Calcular la desviación estándar de todo el array
desviacion_estandar = # TODO: calcular la desviación estándar del array

# 3. Encontrar el valor máximo y mínimo de todo el array
valor_maximo = # TODO: encontrar el valor máximo del array
valor_minimo = # TODO: encontrar el valor mínimo del array

# 4. Calcular la suma de cada fila del array
suma_filas = # TODO: calcular la suma de cada fila del array

# 5. Calcular la media de cada columna del array
media_columnas = # TODO: calcular la media de cada columna del array

# Mostrar el array original y los resultados
print("Array original:")
print(array)
print("\nMedia total:", media_total)
print("Desviación estándar:", desviacion_estandar)
print("Valor máximo:", valor_maximo)
print("Valor mínimo:", valor_minimo)
print("\nSuma de cada fila:")
print(suma_filas)
print("\nMedia de cada columna:")
print(media_columnas)

"""
import numpy as np

# Crear un array NumPy bidimensional de 4x5 con números aleatorios entre 0 y 100
np.random.seed(42)  # Para reproducibilidad
array = np.random.randint(0, 101, size=(4, 5))

# 1. Calcular la media de todo el array
media_total = np.mean(array)

# 2. Calcular la desviación estándar de todo el array
desviacion_estandar = np.std(array)

# 3. Encontrar el valor máximo y mínimo de todo el array
valor_maximo = np.max(array)
valor_minimo = np.min(array)

# 4. Calcular la suma de cada fila del array
suma_filas = np.sum(array, axis=1)

# 5. Calcular la media de cada columna del array
media_columnas = np.mean(array, axis=0)

# Mostrar el array original y los resultados
print("Array original:")
print(array)

print("\nMedia total:", media_total)
print("Desviación estándar:", desviacion_estandar)
print("Valor máximo:", valor_maximo)
print("Valor mínimo:", valor_minimo)

print("\nSuma de cada fila:")
print(suma_filas)

print("\nMedia de cada columna:")
print(media_columnas)
