# Ejercicio 01: Crear Arrays con Numpy
"""
Ejercicio crear arrays con Numpy
Objetivo
Crear diferentes tipos de arrays en NumPy utilizando métodos básicos de creación

Instrucciones
Crea los siguientes arrays de NumPy:

Un array unidimensional con los números del 1 al 10 utilizando array()
Una matriz de ceros de tamaño 3x3 utilizando zeros()
Un array unidimensional con 5 unos utilizando ones()
Un array con 8 valores equidistantes entre 0 y 1 (ambos incluidos) utilizando linspace()
Un array con los números pares del 2 al 20 utilizando arange()
Asegúrate de importar NumPy correctamente al inicio de tu código.

import numpy as np

# 1. Crea un array unidimensional con los números del 1 al 10 mediante array().
array_1_10 = None  # TODO: Sustituye None por el array solicitado.
print("Array unidimensional del 1 al 10:")
print(array_1_10)

# 2. Crea una matriz de ceros de tamaño 3x3 mediante zeros().
matriz_ceros = None  # TODO: Sustituye None por la matriz solicitada.
print("\nMatriz de ceros 3x3:")
print(matriz_ceros)

# 3. Crea un array unidimensional con 5 unos mediante ones().
array_unos = None  # TODO: Sustituye None por el array solicitado.
print("\nArray unidimensional con 5 unos:")
print(array_unos)

# 4. Crea 8 valores equidistantes entre 0 y 1 mediante linspace().
array_equidistante = None  # TODO: Sustituye None por el array solicitado.
print("\nArray con 8 valores equidistantes entre 0 y 1:")
print(array_equidistante)

# 5. Crea los números pares del 2 al 20 mediante arange().
array_pares = None  # TODO: Sustituye None por el array solicitado.
print("\nArray con números pares del 2 al 20:")
print(array_pares)
"""
import numpy as np

# 1. Crea un array unidimensional con los números del 1 al 10 mediante array().
array_1_10 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("Array unidimensional del 1 al 10:")
print(array_1_10)

# 2. Crea una matriz de ceros de tamaño 3x3 mediante zeros().
matriz_ceros = np.zeros((3, 3))

print("\nMatriz de ceros 3x3:")
print(matriz_ceros)

# 3. Crea un array unidimensional con 5 unos mediante ones().
array_unos = np.ones(5)

print("\nArray unidimensional con 5 unos:")
print(array_unos)

# 4. Crea 8 valores equidistantes entre 0 y 1 mediante linspace().
array_equidistante = np.linspace(0, 1, 8)

print("\nArray con 8 valores equidistantes entre 0 y 1:")
print(array_equidistante)

# 5. Crea los números pares del 2 al 20 mediante arange().
array_pares = np.arange(2, 21, 2)

print("\nArray con números pares del 2 al 20:")
print(array_pares)
