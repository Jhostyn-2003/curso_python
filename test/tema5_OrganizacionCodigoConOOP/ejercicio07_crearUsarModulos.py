# Ejercicio 07: Crear y usar módulos
"""
Ejercicio crear y usar módulos
Instrucciones
Escribe el código para un módulo llamado operaciones_matematicas.py que contenga las siguientes funciones:

sumar(a, b): Devuelve la suma de dos números
restar(a, b): Devuelve la resta de dos números
multiplicar(a, b): Devuelve el producto de dos números
dividir(a, b): Devuelve la división de a entre b (debe manejar la división por cero devolviendo un mensaje de error)
Además, define una constante PI con el valor 3.14159.

Luego, escribe el código para un archivo principal calculadora.py que importe el módulo que has creado y realice las siguientes operaciones:

Importa todas las funciones y la constante PI del módulo
Calcula y muestra el resultado de sumar 15 y 7
Calcula y muestra el resultado de multiplicar 3.5 por 2
Calcula y muestra el área de un círculo con radio 5 utilizando la constante PI
Escribe el código python directamente en el editor, no es necesario crear archivos, escribe el código todo seguido en el propio editor.
"""
# ==============================
# operaciones_matematicas.py
# ==============================

PI = 3.14159


def sumar(a, b):
    """Devuelve la suma de dos números."""
    return a + b


def restar(a, b):
    """Devuelve la resta de dos números."""
    return a - b


def multiplicar(a, b):
    """Devuelve el producto de dos números."""
    return a * b


def dividir(a, b):
    """Devuelve la división de a entre b."""
    if b == 0:
        return "Error: no se puede dividir entre cero"

    return a / b


# ==============================
# calculadora.py
# ==============================

# En un proyecto real, esta línea importaría el módulo:
# from operaciones_matematicas import sumar, restar, multiplicar, dividir, PI


resultado_suma = sumar(15, 7)
resultado_multiplicacion = multiplicar(3.5, 2)

radio = 5
area_circulo = PI * radio ** 2

print("Suma de 15 y 7:", resultado_suma)
print("Multiplicación de 3.5 por 2:", resultado_multiplicacion)
print("Área del círculo con radio 5:", area_circulo)