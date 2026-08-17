# Ejercicio 01: Creación de Clase y Objeto
"""
Ejercicio creación de clase y objeto
Objetivo
Crear una clase Persona con atributos y un método para presentarse

Instrucciones
Crea una clase llamada Persona con los siguientes elementos:

Un constructor __init__ que reciba como parámetros nombre y edad y los almacene como atributos de instancia.

Un método llamado presentarse que devuelva un string con el formato: "Hola, me llamo {nombre} y tengo {edad} años".

Luego, crea una instancia de la clase Persona con tu nombre y edad, y llama al método presentarse para verificar que funciona correctamente.
"""
class Persona:
    """
    Representa a una persona con nombre y edad.
    """

    def __init__(self, nombre, edad):
        """
        Inicializa una persona.

        Args:
            nombre (str): Nombre de la persona.
            edad (int): Edad de la persona.
        """
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        """
        Devuelve una presentación de la persona.

        Returns:
            str: Mensaje de presentación.
        """
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años"


persona1 = Persona("Jhostyn", 25)

print(persona1.presentarse())