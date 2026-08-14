# Ejercicio estructuras control iterativo - While
# ejercicio04: Estructura de control iterativo While en Python
"""
Ejercicio estructuras de control iterativo while
Objetivo
Crear un programa que utilice un bucle while para sumar números hasta alcanzar un valor objetivo

Instrucciones
Escribe un programa que sume números enteros positivos ingresados por el usuario hasta alcanzar o superar un valor objetivo de 100. El programa debe:

Inicializar una variable suma en 0 para llevar el registro de la suma acumulada
Utilizar un bucle while que se ejecute mientras la suma sea menor que 100
Dentro del bucle, solicitar al usuario que ingrese un número entero positivo
Si el usuario ingresa un valor no numérico o un número negativo, mostrar un mensaje de error y continuar solicitando un nuevo número sin añadirlo a la suma
Si el número es válido, añadirlo a la suma acumulada y mostrar el valor actual de la suma
Cuando la suma alcance o supere 100, mostrar un mensaje indicando el valor final de la suma y cuántos números válidos fueron ingresados
Puedes comenzar con este esquema:

suma = 0
contador = 0

while suma < 100:
    # Tu código aquí

# Mensaje final
"""
suma = 0
contador = 0

while suma < 100:
    try:
        numero = int(input("Ingresa un número entero positivo: "))

        if numero < 0:
            print("Error: debes ingresar un número positivo.")
            continue

        suma += numero
        contador += 1

        print("Suma actual:", suma)

    except ValueError:
        print("Error: debes ingresar un valor numérico.")

print("La suma final es:", suma)
print("Cantidad de números válidos ingresados:", contador)
