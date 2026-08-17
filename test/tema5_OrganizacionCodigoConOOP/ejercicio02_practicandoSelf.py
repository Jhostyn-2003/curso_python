# Ejercicio 02: Practicando con self
"""
Ejercicio practicando self
Objetivo
Crear una clase con métodos que utilicen self para acceder a atributos de instancia

Instrucciones
Crea una clase llamada Libro con los siguientes requisitos:

El constructor debe inicializar tres atributos de instancia: titulo, autor y páginas.

Implementa un método llamado describir que devuelva un string con el formato: "[Titulo] escrito por [Autor] - [Páginas] páginas".

Implementa un método llamado es_largo que devuelva True si el libro tiene más de 300 páginas, y False en caso contrario.

Implementa un método llamado resumir que reciba un parámetro longitud y devuelva un string con el formato: "[Titulo] - Resumen de [longitud] caracteres". Si no se proporciona el parámetro longitud, debe usar un valor predeterminado de 50.

Prueba tu clase creando al menos dos instancias diferentes de Libro y llamando a todos sus métodos.
"""
class Libro:
    """
    Representa un libro con título, autor y número de páginas.
    """

    def __init__(self, titulo, autor, paginas):
        """
        Inicializa los datos del libro.

        Args:
            titulo (str): Título del libro.
            autor (str): Autor del libro.
            paginas (int): Número de páginas.
        """
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def describir(self):
        """
        Devuelve una descripción del libro.
        """
        return f"{self.titulo} escrito por {self.autor} - {self.paginas} páginas"

    def es_largo(self):
        """
        Indica si el libro tiene más de 300 páginas.
        """
        return self.paginas > 300

    def resumir(self, longitud=50):
        """
        Devuelve un mensaje de resumen con una longitud determinada.

        Args:
            longitud (int): Cantidad de caracteres del resumen.
        """
        return f"{self.titulo} - Resumen de {longitud} caracteres"


# Crear dos objetos de la clase Libro
libro1 = Libro("Don Quijote", "Miguel de Cervantes", 863)
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 96)

# Probar los métodos del primer libro
print(libro1.describir())
print(libro1.es_largo())
print(libro1.resumir())
print(libro1.resumir(100))

# Probar los métodos del segundo libro
print(libro2.describir())
print(libro2.es_largo())
print(libro2.resumir())
print(libro2.resumir(30))
