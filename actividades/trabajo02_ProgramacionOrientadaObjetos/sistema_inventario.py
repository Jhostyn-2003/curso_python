# Trabajo 02 - Programación Orientada a Objetos
"""
Trabajo 2: Python Programación Orientada a Objetos
Pasos
Requisitos
Evaluación
¿Qué hay que hacer?
Desarrollar un sistema básico de inventario con POO en Python para gestionar productos y realizar operaciones de inventario.

Pasos a seguir
Crea un archivo llamado sistema_inventario.py donde implementarás todo el código del sistema.

Define la clase Producto con un método constructor que inicialice los atributos nombre (str), precio (float) y cantidad (int). Incluye validaciones para que el precio sea mayor o igual que cero, el nombre no esté vacío y la cantidad sea mayor o igual a cero.

Añade a la clase Producto los siguientes métodos:

actualizar_precio(nuevo_precio): para modificar el precio validando que sea mayor o igual que cero
actualizar_cantidad(nueva_cantidad): para modificar la cantidad validando que sea mayor o igual a cero
calcular_valor_total(): que devuelva el valor total (precio × cantidad)
__str__(): para mostrar la información del producto de forma legible
Crea la clase Inventario con un constructor que inicialice una lista vacía para almacenar productos.

Implementa en la clase Inventario los siguientes métodos:

agregar_producto(producto): para añadir un objeto de tipo Producto a la lista
buscar_producto(nombre): para encontrar un producto por su nombre (búsqueda exacta, insensible a mayúsculas/minúsculas). Debe devolver el producto si lo encuentra o None si no existe
calcular_valor_inventario(): para sumar el valor total de todos los productos
listar_productos(): para mostrar todos los productos del inventario
Implementa un manejo de excepciones utilizando bloques try-except para capturar errores como valores inválidos (cantidades negativas), tipos de datos incorrectos o productos no encontrados.

Crea una función menu_principal() que muestre opciones al usuario (1. Agregar producto, 2. Buscar producto, 3. Listar productos, 4. Calcular valor total del inventario, 5. Salir) y procese la entrada del usuario en un bucle hasta que elija salir.

En la sección principal del programa (bajo if __name__ == "__main__":), instancia un objeto de la clase Inventario y llama a la función menu_principal() para iniciar la aplicación.

Requisitos
Crear una clase Producto con atributos para nombre, precio y cantidad
Implementar métodos para añadir, actualizar y mostrar información de productos
Desarrollar una clase Inventario que gestione una colección de productos
Implementar operaciones de inventario: añadir producto, buscar por nombre y calcular valor total
Manejar excepciones para entradas inválidas (cantidades negativas, nombres vacíos, etc.)
Crear un menú interactivo simple para probar las funcionalidades
Mostrar resultados de operaciones por consola de manera formateada
Validar que los datos ingresados sean del tipo correcto
Cómo se evalúa
Tu solución se calificará según estos criterios:

Implementación de la clase Producto
30%
Correcta definición de la clase Producto con sus atributos (nombre, precio, cantidad) y métodos (actualizar_precio, actualizar_cantidad, calcular_valor_total, str). Incluye validaciones básicas para los datos.

Implementación de la clase Inventario
30%
Correcta implementación de la clase Inventario con métodos para agregar productos, buscar por nombre, calcular el valor total del inventario y listar todos los productos.

Manejo de excepciones
20%
Implementación de bloques try-except para manejar errores como valores inválidos (cantidades negativas), tipos de datos incorrectos o productos no encontrados.

Interfaz de usuario y funcionalidad
20%
Desarrollo de un menú interactivo que permita al usuario realizar todas las operaciones solicitadas (agregar, buscar, listar productos y calcular valor total).


"""
class Producto:
    """
    Representa un producto dentro del inventario.
    """

    def __init__(self, nombre, precio, cantidad):
        """
        Inicializa un producto.

        Args:
            nombre (str): Nombre del producto.
            precio (float): Precio del producto.
            cantidad (int): Cantidad disponible.
        """
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if not isinstance(precio, (int, float)):
            raise TypeError("El precio debe ser un número.")

        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        if not isinstance(cantidad, int):
            raise TypeError("La cantidad debe ser un número entero.")

        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio):
        """
        Actualiza el precio del producto.
        """
        if not isinstance(nuevo_precio, (int, float)):
            raise TypeError("El precio debe ser un número.")

        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        self.precio = float(nuevo_precio)

    def actualizar_cantidad(self, nueva_cantidad):
        """
        Actualiza la cantidad disponible del producto.
        """
        if not isinstance(nueva_cantidad, int):
            raise TypeError("La cantidad debe ser un número entero.")

        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        self.cantidad = nueva_cantidad

    def calcular_valor_total(self):
        """
        Calcula el valor total del producto.

        Returns:
            float: Precio multiplicado por cantidad.
        """
        return self.precio * self.cantidad

    def __str__(self):
        """
        Devuelve la información del producto de forma legible.
        """
        return (
            f"Producto: {self.nombre} | "
            f"Precio: ${self.precio:.2f} | "
            f"Cantidad: {self.cantidad} | "
            f"Valor total: ${self.calcular_valor_total():.2f}"
        )


class Inventario:
    """
    Gestiona una colección de productos.
    """

    def __init__(self):
        """
        Inicializa un inventario vacío.
        """
        self.productos = []

    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario.
        """
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos de tipo Producto.")

        self.productos.append(producto)

    def buscar_producto(self, nombre):
        """
        Busca un producto por nombre.

        Args:
            nombre (str): Nombre exacto del producto.

        Returns:
            Producto | None: Producto encontrado o None.
        """
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto

        return None

    def calcular_valor_inventario(self):
        """
        Calcula el valor total de todos los productos.

        Returns:
            float: Valor total del inventario.
        """
        total = 0

        for producto in self.productos:
            total += producto.calcular_valor_total()

        return total

    def listar_productos(self):
        """
        Muestra todos los productos del inventario.
        """
        if not self.productos:
            print("El inventario está vacío.")
            return

        print("\n--- PRODUCTOS DEL INVENTARIO ---")

        for producto in self.productos:
            print(producto)


def menu_principal(inventario):
    """
    Muestra y procesa el menú principal del sistema.

    Args:
        inventario (Inventario): Inventario que se gestionará.
    """

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            try:
                nombre = input("Nombre del producto: ").strip()
                precio = float(input("Precio del producto: "))
                cantidad = int(input("Cantidad disponible: "))

                producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(producto)

                print("Producto agregado correctamente.")

            except ValueError as error:
                print(f"Error: {error}")

            except TypeError as error:
                print(f"Error: {error}")

        elif opcion == "2":
            try:
                nombre = input("Nombre del producto a buscar: ").strip()

                if not nombre:
                    raise ValueError("Debes ingresar un nombre.")

                producto = inventario.buscar_producto(nombre)

                if producto is None:
                    raise LookupError("Producto no encontrado.")

                print(producto)

            except (ValueError, LookupError) as error:
                print(f"Error: {error}")

        elif opcion == "3":
            inventario.listar_productos()

        elif opcion == "4":
            total = inventario.calcular_valor_inventario()

            print(f"Valor total del inventario: ${total:.2f}")

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    inventario = Inventario()
    menu_principal(inventario)

