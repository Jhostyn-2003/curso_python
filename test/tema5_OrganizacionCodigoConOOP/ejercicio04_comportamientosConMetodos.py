# Ejercicio 04: Comportamientos con Métodos
"""
Ejercicio comportamiento con métodos
Objetivo
Implementar una clase Contador con métodos de instancia, clase y estáticos

Instrucciones
Crea una clase llamada Contador que gestione un valor numérico. La clase debe implementar:

Un atributo de clase contadores_creados que lleve la cuenta de cuántas instancias se han creado.

Un método de instancia incrementar() que aumente el valor del contador en 1 y devuelva el nuevo valor.

Un método de instancia decrementar() que disminuya el valor del contador en 1 y devuelva el nuevo valor. El contador nunca debe ser negativo.

Un método de clase @classmethod llamado reiniciar_contador_global() que ponga a cero el contador de instancias creadas.

Un método estático @staticmethod llamado es_par(número) que devuelva True si el número proporcionado es par, o False en caso contrario.

Puedes empezar con este esquema:

class Contador:
    # Atributo de clase para contar instancias
    contadores_creados = 0
    
    def __init__(self, valor_inicial=0):
        # Completa el constructor
        pass
        
    # Implementa los métodos requeridos
"""
class Contador:
    """
    Representa un contador numérico.
    """

    contadores_creados = 0

    def __init__(self, valor_inicial=0):
        """
        Inicializa el contador.

        Args:
            valor_inicial (int): Valor inicial del contador.
        """
        self.valor = max(0, valor_inicial)
        Contador.contadores_creados += 1

    def incrementar(self):
        """
        Incrementa el contador en 1.

        Returns:
            int: Nuevo valor del contador.
        """
        self.valor += 1
        return self.valor

    def decrementar(self):
        """
        Disminuye el contador en 1 sin permitir valores negativos.

        Returns:
            int: Nuevo valor del contador.
        """
        if self.valor > 0:
            self.valor -= 1

        return self.valor

    @classmethod
    def reiniciar_contador_global(cls):
        """
        Reinicia el número de contadores creados.
        """
        cls.contadores_creados = 0

    @staticmethod
    def es_par(numero):
        """
        Indica si un número es par.

        Args:
            numero (int): Número a comprobar.

        Returns:
            bool: True si es par, False si es impar.
        """
        return numero % 2 == 0


# Crear dos contadores
contador1 = Contador(5)
contador2 = Contador()

# Métodos de instancia
print("Incrementar:", contador1.incrementar())
print("Decrementar:", contador1.decrementar())

# Comprobar que no sea negativo
print("Decrementar contador2:", contador2.decrementar())

# Cantidad de instancias creadas
print("Contadores creados:", Contador.contadores_creados)

# Método estático
print("¿8 es par?:", Contador.es_par(8))
print("¿7 es par?:", Contador.es_par(7))

# Reiniciar contador global
Contador.reiniciar_contador_global()

print("Contadores creados después de reiniciar:",
      Contador.contadores_creados)