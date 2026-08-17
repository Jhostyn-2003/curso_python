# Ejercicio 03: Variables de Clase y Objetos
"""
Ejercicio variables en clases y objetos
Objetivo
Crear una clase con variables de clase e instancia para gestionar un sistema de biblioteca

Instrucciones
Crea una clase llamada Biblioteca que gestione libros utilizando variables de clase e instancia adecuadamente.

La clase debe tener:

Una variable de clase total_libros inicializada en 0 que lleve la cuenta de todos los libros en el sistema.
Una variable de clase nombre_biblioteca con el valor "Biblioteca Central".
En el método __init__, recibe el parámetro nombre_sección (por ejemplo "Ficción", "Historia", etc.) y crea una variable de instancia para almacenarlo.
En el método __init__, inicializa una variable de instancia libros como una lista vacía para almacenar los libros de esa sección.
Un método agregar_libro(self, titulo) que añada el título a la lista de libros de la sección e incremente la variable de clase total_libros.
Un método obtener_informe(self) que devuelva un string con el formato: "Sección [nombre_sección] de [nombre_biblioteca]: [cantidad] libros".
Finalmente, crea dos instancias de la clase con diferentes secciones, agrega algunos libros a cada una y muestra sus informes para verificar que la variable de clase se comparte correctamente.
"""
class Biblioteca:
    """
    Representa una sección de una biblioteca.
    """

    total_libros = 0
    nombre_biblioteca = "Biblioteca Central"

    def __init__(self, nombre_seccion):
        """
        Inicializa una sección de la biblioteca.

        Args:
            nombre_seccion (str): Nombre de la sección.
        """
        self.nombre_seccion = nombre_seccion
        self.libros = []

    def agregar_libro(self, titulo):
        """
        Agrega un libro a la sección e incrementa el total general.

        Args:
            titulo (str): Título del libro.
        """
        self.libros.append(titulo)
        Biblioteca.total_libros += 1

    def obtener_informe(self):
        """
        Devuelve un informe de la sección.

        Returns:
            str: Información de la sección y cantidad de libros.
        """
        cantidad = len(self.libros)

        return (
            f"Sección {self.nombre_seccion} de "
            f"{Biblioteca.nombre_biblioteca}: {cantidad} libros"
        )


# Crear dos secciones
ficcion = Biblioteca("Ficción")
historia = Biblioteca("Historia")

# Agregar libros a Ficción
ficcion.agregar_libro("Don Quijote")
ficcion.agregar_libro("Cien años de soledad")

# Agregar libros a Historia
historia.agregar_libro("Historia del mundo")
historia.agregar_libro("Historia de Roma")
historia.agregar_libro("Historia antigua")

# Mostrar informes
print(ficcion.obtener_informe())
print(historia.obtener_informe())

# Mostrar el total de libros de toda la biblioteca
print("Total de libros:", Biblioteca.total_libros)