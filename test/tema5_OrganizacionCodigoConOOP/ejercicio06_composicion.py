# Ejercicio 06: Composición
"""
Ejericicio composición
Objetivo
Crear un sistema de biblioteca usando composición en Python

Instrucciones
Implementa un sistema básico de biblioteca utilizando composición. Crea una clase Libro con atributos para título, autor y año de publicación. Luego, crea una clase Biblioteca que contenga una colección de libros (relación "tiene un"). La clase Biblioteca debe incluir métodos para:

Agregar un nuevo libro a la colección
Buscar libros por título (devolviendo todos los que contengan la cadena de búsqueda)
Contar cuántos libros hay de un autor específico
No utilices herencia para resolver este ejercicio, solo composición. Asegúrate de que la clase Biblioteca delegue apropiadamente en los objetos Libro que contiene.
"""
class Libro:
    """
    Representa un libro.
    """

    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion


class Biblioteca:
    """
    Representa una biblioteca que contiene libros.
    """

    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        """
        Agrega un libro a la colección.
        """
        self.libros.append(libro)

    def buscar_por_titulo(self, texto):
        """
        Devuelve los libros cuyo título contiene el texto buscado.
        """
        resultados = []

        for libro in self.libros:
            if texto.lower() in libro.titulo.lower():
                resultados.append(libro)

        return resultados

    def contar_por_autor(self, autor):
        """
        Cuenta cuántos libros pertenecen a un autor.
        """
        contador = 0

        for libro in self.libros:
            if libro.autor.lower() == autor.lower():
                contador += 1

        return contador


# Crear libros
libro1 = Libro("Don Quijote", "Miguel de Cervantes", 1605)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
libro3 = Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", 1985)

# Crear biblioteca
biblioteca = Biblioteca()

# Agregar libros
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Buscar libros por título
resultados = biblioteca.buscar_por_titulo("amor")

for libro in resultados:
    print(libro.titulo)

# Contar libros por autor
cantidad = biblioteca.contar_por_autor("Gabriel García Márquez")

print("Cantidad de libros del autor:", cantidad)