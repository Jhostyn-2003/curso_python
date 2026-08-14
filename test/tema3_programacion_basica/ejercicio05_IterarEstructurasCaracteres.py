# ejercicio05: Iterar estructuras de caracteres en Python
"""
Ejercicio de iterar estructuras de caracteres
Objetivo
Crear un programa que extraiga información específica de una cadena de texto

Instrucciones
Crea una función llamada extraer_info que reciba como parámetro una cadena de texto representando un correo electrónico con el formato nombre@dominio.extensión. La función debe devolver un diccionario con tres claves:

nombre_usuario: la parte del correo antes del símbolo @
dominio: la parte entre @ y el último punto
extensión: la parte después del último punto
Por ejemplo, si la entrada es "usuario@ejemplo.com", la función debe devolver:

{
    "nombre_usuario": "usuario",
    "dominio": "ejemplo",
    "extension": "com"
}
Si la cadena no contiene el símbolo @ o no tiene extensión (un punto después del @), la función debe devolver un diccionario vacío.

Utiliza los métodos de cadenas y técnicas de slicing que has aprendido para resolver este ejercicio.
"""
def extraer_info(correo):
    # Validar que exista el símbolo @
    if "@" not in correo:
        return {}

    # Separar la parte del usuario y el resto del correo
    nombre_usuario, resto = correo.split("@", 1)

    # Validar que exista un punto después del @
    if "." not in resto:
        return {}

    # Buscar el último punto
    posicion_punto = resto.rfind(".")

    # Extraer dominio y extensión usando slicing
    dominio = resto[:posicion_punto]
    extension = resto[posicion_punto + 1:]

    # Validar que la extensión no esté vacía
    if extension == "":
        return {}

    return {
        "nombre_usuario": nombre_usuario,
        "dominio": dominio,
        "extension": extension
    }


resultado = extraer_info("usuario@ejemplo.com")
print(resultado)