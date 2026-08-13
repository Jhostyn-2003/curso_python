# Ejercicio 6: Collections en Python
"""
Ejercicio collections
Objetivo
Crear una función que utilice Counter para analizar frecuencias de caracteres en un texto

Instrucciones
Implementa una función llamada analizar_texto que reciba como parámetro una cadena de texto y devuelva un diccionario con las siguientes estadísticas:

caracteres_mas_comunes: Una lista con los 3 caracteres más comunes y su frecuencia, excluyendo espacios en blanco. El formato debe ser una lista de tuplas (caracter, frecuencia).

total_caracteres: El número total de caracteres en el texto, incluyendo espacios.

total_sin_espacios: El número total de caracteres excluyendo espacios en blanco.

Utiliza la clase Counter del módulo collections para realizar el análisis de frecuencias.

Ejemplo de uso:

resultado = analizar_texto("Hola, mundo! Este es un ejemplo.")
print(resultado)
# Debería imprimir algo como:
# {'caracteres_mas_comunes': [('e', 4), ('o', 3), ('l', 2)], 'total_caracteres': 32, 'total_sin_espacios': 27}
"""
from collections import Counter


def analizar_texto(texto):
    # Contar el total de caracteres incluyendo espacios
    total_caracteres = len(texto)

    # Eliminar espacios en blanco
    texto_sin_espacios = "".join(texto.split())

    # Contar el total de caracteres sin espacios
    total_sin_espacios = len(texto_sin_espacios)

    # Contar la frecuencia de cada carácter
    contador = Counter(texto_sin_espacios)

    # Obtener los 3 caracteres más comunes
    caracteres_mas_comunes = contador.most_common(3)

    # Devolver los resultados en un diccionario
    return {
        "caracteres_mas_comunes": caracteres_mas_comunes,
        "total_caracteres": total_caracteres,
        "total_sin_espacios": total_sin_espacios
    }


resultado = analizar_texto("Hola, mundo! Este es un ejemplo.")

print(resultado)