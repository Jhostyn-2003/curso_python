# Ejercicio 4: Diccionarios en Python
"""
Ejercicio diccionarios
Objetivo
Crear un diccionario para almacenar información de contactos y acceder a sus datos

Instrucciones
Crea un diccionario llamado contactos que contenga la información de tres personas. Para cada persona, almacena su nombre, teléfono y correo electrónico. Luego, realiza las siguientes operaciones:

Muestra el correo electrónico de la segunda persona que añadiste al diccionario.
Añade un nuevo contacto con la información que prefieras.
Modifica el número de teléfono de la primera persona que añadiste.
Utiliza un bucle para mostrar los nombres de todos los contactos.
Puedes empezar con algo como:

contactos = {
    "persona1": {"nombre": "Ana", "telefono": "123456789", "email": "ana@ejemplo.com"},
    # Añade más contactos aquí
}

# Tu código para realizar las operaciones solicitadas

"""
# Diccionario con tres contactos
contactos = {
    "persona1": {
        "nombre": "Ana",
        "telefono": "123456789",
        "email": "ana@ejemplo.com"
    },
    "persona2": {
        "nombre": "Carlos",
        "telefono": "987654321",
        "email": "carlos@ejemplo.com"
    },
    "persona3": {
        "nombre": "María",
        "telefono": "555123456",
        "email": "maria@ejemplo.com"
    }
}

# 1. Mostrar el correo electrónico de la segunda persona
print("Correo de la segunda persona:", contactos["persona2"]["email"])

# 2. Añadir un nuevo contacto
contactos["persona4"] = {
    "nombre": "Luis",
    "telefono": "444555666",
    "email": "luis@ejemplo.com"
}

# 3. Modificar el número de teléfono de la primera persona
contactos["persona1"]["telefono"] = "111222333"

# 4. Mostrar los nombres de todos los contactos
for persona in contactos.values():
    print(persona["nombre"])