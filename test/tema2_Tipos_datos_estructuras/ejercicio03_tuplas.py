# Ejercicio 3: Tuplas en Python
"""
Ejercicio tuplas
Objetivo
Crear y manipular una tupla con información de contactos

Instrucciones
Crea una tupla llamada contacto que contenga la siguiente información en este orden: nombre, correo electrónico y número de teléfono. Utiliza los valores "Ana García", "ana@ejemplo.com" y "555-1234".

Luego, realiza las siguientes operaciones:

Desempaqueta la tupla en tres variables llamadas nombre, email y telefono.
Imprime cada variable en líneas separadas.
Crea una nueva tupla llamada contacto_completo que contenga los elementos de la tupla original más la ciudad "Madrid" al final.
Recuerda que las tuplas son inmutables, por lo que deberás crear una nueva tupla para añadir el elemento adicional.
"""
# Tupla original con la información del contacto
contacto = ("Ana García", "ana@ejemplo.com", "555-1234")

# 1. Desempaquetar la tupla
nombre, email, telefono = contacto

# 2. Imprimir cada variable
print("Nombre:", nombre)
print("Email:", email)
print("Teléfono:", telefono)

# 3. Crear una nueva tupla agregando la ciudad
contacto_completo = contacto + ("Madrid",)

# Mostrar la nueva tupla
print("Contacto completo:", contacto_completo)