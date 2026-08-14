# Ejercicio 2: Listas en Python
"""
Ejercicio listas
Objetivo
Crear y manipular una lista de números para calcular estadísticas básicas

Instrucciones
Crea una lista llamada números que contenga los valores 10, 20, 30, 40 y 50. A continuación, realiza las siguientes operaciones:

Añade el número 60 al final de la lista
Inserta el número 15 entre el 10 y el 20
Elimina el número 30 de la lista
Calcula la suma de todos los números en la lista y guárdala en una variable llamada suma
Calcula el promedio de los números en la lista y guárdalo en una variable llamada promedio
Al final, imprime la lista resultante, la suma y el promedio.
"""
numeros = [10, 20, 30, 40, 50]

# 1. Añadir 60 al final
numeros.append(60)

# 2. Insertar 15 entre 10 y 20
numeros.insert(1, 15)

# 3. Eliminar el número 30
numeros.remove(30)

# 4. Calcular la suma
suma = sum(numeros)

# 5. Calcular el promedio
promedio = suma / len(numeros)

# Mostrar resultados
print("Lista resultante:", numeros)
print("Suma:", suma)
print("Promedio:", promedio)