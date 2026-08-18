# Ejercicio 02 - Filtrar y transformar datos
"""
Ejercicio de filtrar y transformar datos
Objetivo
Filtrar números pares y duplicarlos usando filter() y map()

Instrucciones
Dada una lista de números enteros, crea una función llamada procesar_numeros que realice las siguientes operaciones:

Filtra solo los números pares de la lista usando la función filter()
Aplica una transformación a cada número par para duplicar su valor usando la función map()
Devuelve una lista con los resultados
Por ejemplo, si la entrada es [1, 2, 3, 4, 5, 6], la salida debe ser [4, 8, 12] (los números pares 2, 4 y 6 filtrados y luego duplicados).
"""
def procesar_numeros(numeros):
    """
    Filtra los números pares y duplica su valor.

    Args:
        numeros (list): Lista de números enteros.

    Returns:
        list: Lista con los números pares duplicados.
    """
    pares = filter(lambda numero: numero % 2 == 0, numeros)
    duplicados = map(lambda numero: numero * 2, pares)

    return list(duplicados)


resultado = procesar_numeros([1, 2, 3, 4, 5, 6])

print(resultado)


