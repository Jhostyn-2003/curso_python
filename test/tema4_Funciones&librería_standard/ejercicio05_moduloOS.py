# Ejercicio 05: Módulo os
"""
Ejercicio módulo os
Objetivo
Crear un script que liste archivos por tamaño en un directorio

Instrucciones
Crea un script en Python que utilice el módulo os para listar todos los archivos (no directorios) en el directorio actual, ordenados por tamaño (de mayor a menor). Para cada archivo, muestra su nombre y tamaño en bytes.

El script debe:

Obtener la lista de todos los elementos en el directorio actual
Filtrar solo los archivos (no directorios)
Obtener el tamaño de cada archivo usando las funciones apropiadas
Ordenar la lista de archivos por tamaño de forma descendente
Mostrar el nombre y tamaño de cada archivo
Puedes empezar importando el módulo os y utilizando os.listdir() para obtener los elementos del directorio actual.
"""
import os


def listar_archivos_por_tamano():
    """
    Lista los archivos del directorio actual ordenados
    por tamaño de mayor a menor.
    """
    archivos = []

    for elemento in os.listdir():
        if os.path.isfile(elemento):
            tamano = os.path.getsize(elemento)
            archivos.append((elemento, tamano))

    archivos.sort(key=lambda archivo: archivo[1], reverse=True)

    for nombre, tamano in archivos:
        print(f"{nombre}: {tamano} bytes")


listar_archivos_por_tamano()