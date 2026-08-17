# Trabajo 02 - Programacion Orientada a Objetos

## Descripcion
Este trabajo implementa un sistema basico de inventario en Python aplicando Programacion Orientada a Objetos (POO).

El sistema permite:

- Registrar productos con validaciones.
- Buscar productos por nombre.
- Listar todos los productos almacenados.
- Calcular el valor total del inventario.
- Interactuar mediante un menu en consola.

Implementacion principal en:

- sistema_inventario.py

## Resultado de evaluacion

- Calificacion global: 10/10
- Estado: Superado

### Criterios evaluados

1. Implementacion de la clase Producto: 10/10
2. Implementacion de la clase Inventario: 10/10
3. Manejo de excepciones: 10/10
4. Interfaz de usuario y funcionalidad: 10/10

## Estructura del sistema

### Clase Producto
Representa cada producto del inventario.

**Atributos:**

- nombre (str)
- precio (float)
- cantidad (int)

**Validaciones en el constructor:**

- nombre debe ser texto y no estar vacio.
- precio debe ser numerico y mayor o igual que 0.
- cantidad debe ser entera y mayor o igual que 0.

**Metodos:**

- actualizar_precio(nuevo_precio)
- actualizar_cantidad(nueva_cantidad)
- calcular_valor_total()
- __str__()

### Clase Inventario
Administra la coleccion de productos.

**Atributo:**

- productos (lista de objetos Producto)

**Metodos:**

- agregar_producto(producto)
- buscar_producto(nombre)
- calcular_valor_inventario()
- listar_productos()

## Manejo de errores
El programa usa try-except para controlar errores de entrada y de negocio:

- ValueError: datos invalidos (por ejemplo, negativos o nombre vacio).
- TypeError: tipos de datos incorrectos.
- LookupError: producto no encontrado en busqueda.

Esto evita caidas del programa y mejora la experiencia del usuario.

## Menu interactivo
La funcion menu_principal(inventario) mantiene un bucle con estas opciones:

1. Agregar producto
2. Buscar producto
3. Listar productos
4. Calcular valor total del inventario
5. Salir

En el bloque principal se crea una instancia de Inventario y se inicia el menu.

## Como ejecutar
Desde la carpeta del proyecto, ejecuta:

```bash
python actividades/trabajo02_ProgramacionOrientadaObjetos/sistema_inventario.py
```

## Ejemplo de uso

```text
===== SISTEMA DE INVENTARIO =====
1. Agregar producto
2. Buscar producto
3. Listar productos
4. Calcular valor total del inventario
5. Salir
```

## Aspectos destacados del trabajo

- Codigo claro, coherente y alineado con el enunciado.
- Validaciones completas en Producto.
- Busqueda por nombre insensible a mayusculas/minusculas.
- Salida en consola legible y formateada.
- Cumplimiento total de los requisitos funcionales.

## Mejoras opcionales futuras
Estas mejoras no eran obligatorias para la nota, pero podrian añadirse:

- Agregar anotaciones de tipo en las firmas de metodos y constructor.
- Permitir precios como cadenas numericas (por ejemplo "10.5") convirtiendolas a float.