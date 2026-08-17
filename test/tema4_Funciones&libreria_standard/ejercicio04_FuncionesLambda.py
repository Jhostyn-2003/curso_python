# Ejercicio 04: Funciones lambda
"""
Ejercicio crear funciones lambda
Objetivo
Crear funciones lambda para procesar una lista de números

Instrucciones
Crea tres funciones lambda y asígnalas a variables con los siguientes nombres y comportamientos:

cuadrado: una función que reciba un número y devuelva su cuadrado.
es_par: una función que reciba un número y devuelva True si es par o False si es impar.
suma: una función que reciba dos números y devuelva su suma.
Luego, crea una lista llamada números con los valores [1, 2, 3, 4, 5] y utiliza la función map() con tu lambda cuadrado para crear una nueva lista llamada cuadrados que contenga el cuadrado de cada número.

Finalmente, utiliza la función filter() con tu lambda es_par para crear una lista llamada pares que contenga solo los números pares de la lista original.

"""
# Función lambda que devuelve el cuadrado de un número
cuadrado = lambda numero: numero ** 2

# Función lambda que verifica si un número es par
es_par = lambda numero: numero % 2 == 0

# Función lambda que suma dos números
suma = lambda numero1, numero2: numero1 + numero2

# Lista original
numeros = [1, 2, 3, 4, 5]

# Crear una lista con los cuadrados usando map()
cuadrados = list(map(cuadrado, numeros))

# Crear una lista con los números pares usando filter()
pares = list(filter(es_par, numeros))

# Mostrar resultados
print("Números:", numeros)
print("Cuadrados:", cuadrados)
print("Pares:", pares)
print("Ejemplo de suma:", suma(5, 3))