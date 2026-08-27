# Curso de Python para Certificacion

Repositorio academico con ejercicios, practicas y trabajos de evaluacion desarrollados durante el **Curso de Python**.

El proyecto recoge el aprendizaje progresivo del lenguaje: desde la sintaxis y la programacion estructurada hasta la programacion orientada a objetos, el analisis de datos y la visualizacion de informacion.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-analisis%20numerico-013243?logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-manipulacion%20de%20datos-150458?logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-visualizacion-11557C)
![Seaborn](https://img.shields.io/badge/Seaborn-graficos-4C72B0)

## Indice

- [Curso de Python para Certificacion](#curso-de-python-para-certificacion)
  - [Indice](#indice)
  - [Objetivos](#objetivos)
  - [Trabajos practicos](#trabajos-practicos)
    - [Trabajo 1: Sintaxis Python](#trabajo-1-sintaxis-python)
    - [Trabajo 2: Programacion Orientada a Objetos](#trabajo-2-programacion-orientada-a-objetos)
    - [Trabajo 3: Analisis de datos con NumPy y Pandas](#trabajo-3-analisis-de-datos-con-numpy-y-pandas)
    - [Trabajo 4: Visualizacion de datos](#trabajo-4-visualizacion-de-datos)
  - [Temario y ejercicios](#temario-y-ejercicios)
  - [Estructura del repositorio](#estructura-del-repositorio)
  - [Instalacion y ejecucion](#instalacion-y-ejecucion)
  - [Tecnologias](#tecnologias)
  - [Autor](#autor)

## Objetivos

- Consolidar los fundamentos de Python y la escritura de codigo legible.
- Aplicar estructuras de control, funciones, colecciones y manejo de excepciones.
- Modelar problemas mediante clases, objetos, herencia y composicion.
- Analizar datos con NumPy y Pandas mediante operaciones estadisticas y transformaciones.
- Comunicar resultados mediante graficos creados con Matplotlib y Seaborn.
- Mantener una organizacion de proyecto reproducible y facil de consultar.

## Trabajos practicos

| Trabajo | Contenido | Archivo o carpeta principal |
| --- | --- | --- |
| **Trabajo 1** | Sintaxis Python y programacion estructurada | [`calculadora_promedios.py`](actividades/trabajo01_sintaxis_python/calculadora_promedios.py) |
| **Trabajo 2** | Programacion Orientada a Objetos | [`sistema_inventario.py`](actividades/trabajo02_ProgramacionOrientadaObjetos/sistema_inventario.py) |
| **Trabajo 3** | Analisis de datos con NumPy y Pandas | [`analisis_red_tiendas.ipynb`](actividades/trabajo03_AnalisisDatosConNumpyyPandas/python_intermedio/analisis_red_tiendas.ipynb) |
| **Trabajo 4** | Visualizacion con Matplotlib y Seaborn | [`trabajo4_visualizacion.ipynb`](actividades/trabajo04_VisualizacionDatosConMatplotlibySeaborn/trabajo4_visualizacion.ipynb) |

### Trabajo 1: Sintaxis Python

Calculadora de promedios escolares desarrollada con programacion estructurada. Permite registrar materias y calificaciones, validar entradas, calcular el promedio, clasificar resultados y localizar las calificaciones maxima y minima.

### Trabajo 2: Programacion Orientada a Objetos

Sistema de inventario en consola basado en las clases `Producto` e `Inventario`. Incluye validaciones, busqueda por nombre, listado de productos, calculo del valor total y manejo de excepciones.

### Trabajo 3: Analisis de datos con NumPy y Pandas

Notebook de analisis del caso **RetailNow**. Procesa ventas, inventarios y satisfaccion de clientes para obtener indicadores por producto y tienda, estadisticas descriptivas, inventarios criticos, correlaciones y una simulacion reproducible de ventas futuras.

### Trabajo 4: Visualizacion de datos

Notebook basado en el dataset `superstore_dataset2012.csv`. Incluye histogramas, boxplots, dispersion, regresion, mapa de correlaciones y una figura final con multiples subplots. Los resultados se guardan en `resultados/`.

## Temario y ejercicios

La carpeta `test/` contiene ejercicios de practica organizados por bloques:

| Tema | Contenidos principales |
| --- | --- |
| **Tema 1. Introduccion** | Bienvenida al curso y comprobacion de la version de Python |
| **Tema 2. Tipos de datos y estructuras** | Tipos basicos, listas, tuplas, diccionarios, conjuntos y `collections` |
| **Tema 3. Programacion basica** | Operadores, condicionales, bucles e iteracion de estructuras |
| **Tema 4. Funciones y libreria estandar** | Funciones, argumentos, `lambda`, datos aleatorios y modulo `os` |
| **Tema 5. Organizacion del codigo con POO** | Clases, objetos, atributos, metodos, herencia, composicion y modulos |
| **Tema 6. Aspectos avanzados** | Excepciones, filtrado, transformacion, comprensiones, iteradores y generadores |
| **Tema 7. Analisis de datos** | Arrays con NumPy y DataFrames, filtrado, combinacion, estadistica y tablas pivotantes |
| **Tema 8. Visualizacion de datos** | Graficos univariantes, bivariantes y multivariantes con Matplotlib y Seaborn |

## Estructura del repositorio

```text
curso_python/
├── actividades/
│   ├── trabajo01_sintaxis_python/
│   ├── trabajo02_ProgramacionOrientadaObjetos/
│   ├── trabajo03_AnalisisDatosConNumpyyPandas/
│   └── trabajo04_VisualizacionDatosConMatplotlibySeaborn/
├── test/
│   ├── tema1_introduccion/
│   ├── tema2_Tipos_datos_estructuras/
│   ├── tema3_programacion_basica/
│   ├── tema4_Funciones&libreria_standard/
│   ├── tema5_OrganizacionCodigoConOOP/
│   ├── tema6_aspectosAvanzados/
│   ├── tema7_AnalisisDatosConNumpy&Pandas/
│   └── tema8_VisualizacionDatosConMatplotlibySeaborn/
└── README.md
```

## Instalacion y ejecucion

Se recomienda utilizar un entorno virtual para aislar las dependencias:

```bash
python -m venv .venv
```

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

En macOS o Linux:

```bash
source .venv/bin/activate
```

Para ejecutar los trabajos escritos en Python:

```bash
python actividades/trabajo01_sintaxis_python/calculadora_promedios.py
python actividades/trabajo02_ProgramacionOrientadaObjetos/sistema_inventario.py
```

Los trabajos 3 y 4 se ejecutan como notebooks desde Visual Studio Code o Jupyter, seleccionando el entorno virtual como kernel. Sus dependencias principales son `numpy`, `pandas`, `matplotlib` y `seaborn`.

## Tecnologias

- **Python 3.x**: lenguaje principal.
- **NumPy**: calculo numerico y simulaciones.
- **Pandas**: limpieza, transformacion y analisis de datos.
- **Matplotlib**: visualizaciones personalizadas.
- **Seaborn**: visualizaciones estadisticas.
- **Jupyter Notebook**: desarrollo y presentacion de los analisis.

## Autor

**Jhostyn Gavilanbez**

Repositorio desarrollado con fines academicos para la certificacion del Curso de Python.
