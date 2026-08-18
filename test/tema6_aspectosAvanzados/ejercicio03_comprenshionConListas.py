# Ejercicio 03 - Comprensión con listas
"""
Ejercicio de comprehensions con listas
Objetivo
Crear una lista de palabras en mayúsculas que tengan más de 4 letras

Instrucciones
Dada la siguiente lista de palabras: ["python", "programación", "lista", "comprehensión", "for", "if", "else", "diccionario"]

Utiliza una list comprehensión para crear una nueva lista que contenga solo las palabras que tienen más de 4 letras, y además, convierte estas palabras a mayúsculas.

Por ejemplo, si la lista original fuera ["hola", "mundo", "python"], el resultado sería ["MUNDO", "PYTHON"] porque "hola" tiene 4 letras exactamente y no cumple la condición de tener más de 4 letras.
"""

palabras = [
    "python",
    "programación",
    "lista",
    "comprehensión",
    "for",
    "if",
    "else",
    "diccionario"
]

resultado = [palabra.upper() for palabra in palabras if len(palabra) > 4]

print(resultado)
