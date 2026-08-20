# Ejercicio 02: Atributos de Arrays en Numpy
"""
Ejercicio atributos de arrays en Numpy
Objetivo
Crear un programa que analice y muestre las propiedades de un array NumPy

Instrucciones
Crea un programa que genere un array NumPy tridimensional de tamaño 4x3x2 con valores aleatorios enteros entre 1 y 100. Luego, muestra por pantalla la siguiente información sobre el array:

La forma (shape) del array
El número de dimensiones (ndim) del array
El número total de elementos (size) del array
El tipo de datos (dtype) del array
El tamaño en bytes de cada elemento (itemsize) del array
El tamaño total en bytes (nbytes) del array
Finalmente, verifica e imprime si el tamaño total en bytes (nbytes) es igual al producto del número de elementos (size) por el tamaño de cada elemento (itemsize).

import numpy as np

# Crear un array NumPy tridimensional de tamaño 4x3x2 con valores aleatorios enteros entre 1 y 100
array_3d = np.random.randint(1, 101, size=(4, 3, 2))

# Mostrar el array generado
print("Array generado:")
print(array_3d)
print("\n")

# 1. Mostrar la forma (shape) del array
# TODO: Imprimir la forma del array

# 2. Mostrar el número de dimensiones (ndim) del array
# TODO: Imprimir el número de dimensiones del array

# 3. Mostrar el número total de elementos (size) del array
# TODO: Imprimir el número total de elementos del array

# 4. Mostrar el tipo de datos (dtype) del array
# TODO: Imprimir el tipo de datos del array

# 5. Mostrar el tamaño en bytes de cada elemento (itemsize) del array
# TODO: Imprimir el tamaño en bytes de cada elemento del array

# 6. Mostrar el tamaño total en bytes (nbytes) del array
# TODO: Imprimir el tamaño total en bytes del array

# Verificar si nbytes es igual a size * itemsize
# TODO: Verificar e imprimir si el tamaño total en bytes es igual al producto del número de elementos por el tamaño de cada elemento
"""
import numpy as np

# Crear un array NumPy tridimensional de tamaño 4x3x2
# con valores aleatorios enteros entre 1 y 100
array_3d = np.random.randint(1, 101, size=(4, 3, 2))

# Mostrar el array generado
print("Array generado:")
print(array_3d)
print("\n")

# 1. Mostrar la forma (shape) del array
print("Forma del array:", array_3d.shape)

# 2. Mostrar el número de dimensiones (ndim) del array
print("Número de dimensiones:", array_3d.ndim)

# 3. Mostrar el número total de elementos (size) del array
print("Número total de elementos:", array_3d.size)

# 4. Mostrar el tipo de datos (dtype) del array
print("Tipo de datos:", array_3d.dtype)

# 5. Mostrar el tamaño en bytes de cada elemento (itemsize)
print("Tamaño de cada elemento en bytes:", array_3d.itemsize)

# 6. Mostrar el tamaño total en bytes (nbytes)
print("Tamaño total en bytes:", array_3d.nbytes)

# Verificar si nbytes es igual a size * itemsize
verificacion = array_3d.nbytes == array_3d.size * array_3d.itemsize

print(
    "¿nbytes es igual a size * itemsize?:",
    verificacion
)
