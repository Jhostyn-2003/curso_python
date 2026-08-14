# Tema 3. Programación básica
# Ejercicio 1: Operadores en Python
"""
Ejercicio operadores
Objetivo
Crea una calculadora básica que utilice operadores aritméticos para realizar operaciones matemáticas.

Instrucciones
Crea una calculadora básica que realice las cuatro operaciones aritméticas fundamentales (suma, resta, multiplicación y división) entre dos números.

Debes solicitar al usuario que introduzca dos números y luego mostrar el resultado de las cuatro operaciones con estos números.

Para cada operación, muestra el resultado con el siguiente formato:

"La suma de X y Y es: Z"
"La resta de X y Y es: Z"
"La multiplicación de X y Y es: Z"
"La división de X y Y es: Z"
Recuerda manejar el caso especial de división por cero mostrando un mensaje apropiado.

Pista: Utiliza los operadores +, -, *, / y controla la división por cero con una estructura condicional.
"""
# Solicitar los dos números al usuario
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Realizar las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

# Mostrar resultados
print(f"La suma de {numero1} y {numero2} es: {suma}")
print(f"La resta de {numero1} y {numero2} es: {resta}")
print(f"La multiplicación de {numero1} y {numero2} es: {multiplicacion}")

# Controlar la división por cero
if numero2 != 0:
    division = numero1 / numero2
    print(f"La división de {numero1} y {numero2} es: {division}")
else:
    print("No se puede dividir entre cero.")
