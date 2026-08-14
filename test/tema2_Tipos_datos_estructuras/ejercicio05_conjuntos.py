# Ejercicio 5: Conjuntos en Python
"""
Ejercicio conjuntos
Objetivo
Crear un programa que utilice conjuntos para encontrar elementos comunes y únicos entre dos listas

Instrucciones
Crea un programa que trabaje con dos listas de números enteros. Debes convertir estas listas a conjuntos y realizar las siguientes operaciones:

Encuentra los elementos que aparecen en ambas listas (intersección)
Encuentra los elementos que solo aparecen en la primera lista (diferencia)
Encuentra los elementos que solo aparecen en la segunda lista (diferencia)
Encuentra todos los elementos únicos que aparecen en cualquiera de las dos listas (unión)
Utiliza las siguientes listas para tu programa:

lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [4, 5, 6, 7, 8, 9]
Imprime el resultado de cada operación en líneas separadas.
"""
# Listas originales
lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [4, 5, 6, 7, 8, 9]

# Convertir las listas a conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

# 1. Elementos que aparecen en ambas listas
interseccion = conjunto1 & conjunto2

# 2. Elementos que solo aparecen en la primera lista
solo_lista1 = conjunto1 - conjunto2

# 3. Elementos que solo aparecen en la segunda lista
solo_lista2 = conjunto2 - conjunto1

# 4. Todos los elementos únicos de ambas listas
union = conjunto1 | conjunto2

# Mostrar resultados
print("Intersección:", interseccion)
print("Solo en lista1:", solo_lista1)
print("Solo en lista2:", solo_lista2)
print("Unión:", union)