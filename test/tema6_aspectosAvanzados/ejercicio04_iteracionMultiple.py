# Ejercicio 04 - Iteración múltiple
"""
Ejercicio de iteración múltiple
Objetivo
Crear una matriz de multiplicación con bucles anidados

Instrucciones
Crea una matriz de multiplicación de 5x5 utilizando bucles anidados. La matriz debe contener el resultado de multiplicar el número de fila por el número de columna. Por ejemplo, en la posición [2][3] debe estar el valor 6 (2×3). Después de crear la matriz, muestra su contenido en la consola con un formato de tabla, donde cada fila aparezca en una línea diferente y los números estén separados por espacios.
"""

matriz = []

for fila in range(1, 6):
    nueva_fila = []

    for columna in range(1, 6):
        nueva_fila.append(fila * columna)

    matriz.append(nueva_fila)


for fila in matriz:
    for valor in fila:
        print(valor, end=" ")

    print()

