# Ejercicio 02: Crear funciones
"""
Ejercicio crear funciones
Objetivo
Crear una función que calcule el área de un rectángulo

Instrucciones
Crea una función llamada calcular_area_rectangulo que reciba dos parámetros: base y altura. La función debe calcular y retornar el área del rectángulo (base × altura).

Luego, llama a la función con los valores 5 y 3, y almacena el resultado en una variable llamada area. Finalmente, imprime el resultado con un mensaje descriptivo.
"""
def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    Args:
        base (float): Base del rectángulo.
        altura (float): Altura del rectángulo.

    Returns:
        float: Área del rectángulo.
    """
    return base * altura


area = calcular_area_rectangulo(5, 3)

print("El área del rectángulo es:", area)
