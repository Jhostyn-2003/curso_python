# Curso Python

Repositorio de ejercicios de Python para la certificacion.

## Estructura

- `calculadora_promedios.py`: implementacion del Ejercicio 1.

## Ejercicio 1: Trabajo 1 - Sintaxis Python

Archivo de referencia: `calculadora_promedios.py`

### Que hay que hacer

Desarrollar una calculadora de promedios escolares en Python utilizando variables, operadores, estructuras de control y funciones basicas.

### Pasos a seguir

1. Crear un archivo Python llamado `calculadora_promedios.py` que contenga todo el codigo del programa.
2. Implementar una funcion llamada `ingresar_calificaciones()` que permita al usuario introducir el nombre de una materia y su calificacion correspondiente. Esta funcion debe:
- Solicitar al usuario que ingrese el nombre de la materia.
- Solicitar la calificacion, validando que sea un numero entre 0 y 10.
- Almacenar ambos datos en dos listas separadas (una para nombres y otra para calificaciones).
- Preguntar si desea continuar ingresando mas materias.
- Retornar ambas listas cuando el usuario decida terminar.
3. Crear una funcion `calcular_promedio(calificaciones)` que reciba una lista de calificaciones y devuelva el promedio de todas ellas.
4. Desarrollar una funcion `determinar_estado(calificaciones, umbral)` que reciba la lista de calificaciones y un valor umbral (por defecto 5.0), y devuelva dos listas: una con los indices de las materias aprobadas y otra con los indices de las reprobadas.
5. Implementar una funcion `encontrar_extremos(calificaciones)` que identifique el indice de la calificacion mas alta y el indice de la mas baja en la lista de calificaciones.
6. En la funcion principal (`main`), llamar a `ingresar_calificaciones()` para obtener los datos del usuario.
7. Utilizar las funciones creadas para calcular el promedio general, determinar materias aprobadas/reprobadas y encontrar las materias con calificaciones extremas.
8. Mostrar un resumen final que incluya:
- Todas las materias con sus calificaciones.
- El promedio general.
- Las materias aprobadas y reprobadas.
- La materia con mejor calificacion y su valor.
- La materia con peor calificacion y su valor.
9. Manejar casos especiales, como cuando no se ingresa ninguna materia, utilizando estructuras condicionales apropiadas.
10. Finalizar el programa con un mensaje de despedida e implementar la estructura `if __name__ == "__main__":` para ejecutar la funcion principal.

### Requisitos

- Crear un programa que permita al usuario ingresar nombres de materias y sus calificaciones correspondientes (valores entre 0 y 10).
- Almacenar las materias y calificaciones en estructuras de datos adecuadas (listas).
- Calcular y mostrar el promedio general de todas las calificaciones ingresadas.
- Determinar que materias estan aprobadas y reprobadas segun un umbral definido (5.0).
- Identificar y mostrar la materia con la calificacion mas alta y la mas baja.
- Permitir al usuario agregar tantas materias como desee, con opcion para finalizar la entrada de datos.
- Mostrar un resumen final con toda la informacion procesada de forma clara.
- Utilizar exclusivamente programacion estructurada (sin clases ni POO).
- Implementar al menos 3 funciones diferentes para organizar el codigo.
- Incluir validacion basica de entradas para evitar errores.

### Como se evalua

Tu solucion se calificara segun estos criterios:

1. Implementacion de funciones y estructura (30%)
	Correcta implementacion de las funciones solicitadas (`ingresar_calificaciones`, `calcular_promedio`, `determinar_estado`, `encontrar_extremos`) y organizacion adecuada del codigo sin usar POO.

2. Manejo de estructuras de datos (25%)
	Uso adecuado de listas para almacenar y manipular las materias y calificaciones, incluyendo la correcta indexacion y acceso a los elementos.

3. Calculos y logica (25%)
	Implementacion correcta de los calculos de promedio, determinacion de aprobados/reprobados segun umbral, e identificacion de materias con calificacion maxima y minima.

4. Validacion de entrada y manejo de errores (20%)
	Validacion adecuada de las entradas del usuario (calificaciones entre 0 y 10, conversion de tipos) y manejo de posibles errores o casos especiales.

### Tecnologias a utilizar

![Python](https://certidevs-campus.s3.amazonaws.com/techs/1766999139868-Python-logo.svg)

Python

## Proximos ejercicios

Este README quedo preparado para agregar nuevos ejercicios en secciones `## Ejercicio 2`, `## Ejercicio 3`, etc.

## Autor

Jhostyn Gavilanbez


