# Ejercicio 05: Herencia
"""
Ejercicio de herencia
Objetivo
Crear una jerarquía de clases para modelar diferentes tipos de vehículos

Instrucciones
Crea una jerarquía de clases para modelar vehículos. Debes implementar:

Una clase base Vehículo con los siguientes atributos y métodos:
Atributos: marca, modelo y año
Un método mostrar_info() que devuelva un string con la información básica del vehículo
Una clase derivada Automovil que herede de Vehículo y añada:
Un atributo adicional puertas (número de puertas)
Sobrescribe el método mostrar_info() para incluir el número de puertas
Una clase derivada Motocicleta que herede de Vehículo y añada:
Un atributo adicional cilindrada (en cc)
Sobrescribe el método mostrar_info() para incluir la cilindrada
Finalmente, crea una instancia de cada clase derivada y muestra su información usando el método mostrar_info().
"""
class Vehiculo:
    """
    Representa un vehículo de forma general.
    """

    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def mostrar_info(self):
        """
        Devuelve la información básica del vehículo.
        """
        return f"{self.marca} {self.modelo}, año {self.anio}"


class Automovil(Vehiculo):
    """
    Representa un automóvil.
    """

    def __init__(self, marca, modelo, anio, puertas):
        super().__init__(marca, modelo, anio)
        self.puertas = puertas

    def mostrar_info(self):
        """
        Devuelve la información del automóvil.
        """
        return f"{super().mostrar_info()} - {self.puertas} puertas"


class Motocicleta(Vehiculo):
    """
    Representa una motocicleta.
    """

    def __init__(self, marca, modelo, anio, cilindrada):
        super().__init__(marca, modelo, anio)
        self.cilindrada = cilindrada

    def mostrar_info(self):
        """
        Devuelve la información de la motocicleta.
        """
        return f"{super().mostrar_info()} - {self.cilindrada} cc"


# Crear objetos
automovil = Automovil("Toyota", "Corolla", 2024, 4)
motocicleta = Motocicleta("Yamaha", "MT-07", 2023, 689)

# Mostrar información
print(automovil.mostrar_info())
print(motocicleta.mostrar_info())