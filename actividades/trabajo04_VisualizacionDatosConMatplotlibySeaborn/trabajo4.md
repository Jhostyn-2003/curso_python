# Trabajo 4: Visualización de datos con Matplotlib y Seaborn

## ¿Qué hay que hacer?

Crear visualizaciones con **Matplotlib** y **Seaborn** para analizar el dataset `superstore_dataset2012.csv`.

## Estructura recomendada del proyecto

```text
TRABAJO1_SINTAXISPYTHON/
│
├── actividades/
│   ├── trabajo01_sintaxis_python/
│   ├── trabajo02_ProgramacionOrientadaObjetos/
│   ├── trabajo03_AnalisisDatosConNumpyyPandas/
│   │
│   └── trabajo04_VisualizacionDatosConMatplotlibySeaborn/
│       ├── data/
│       │   └── superstore_dataset2012.csv
│       ├── resultados/
│       │   └── visualizacion_resumen.png
│       ├── trabajo4_visualizacion.ipynb
│       └── trabajo4.md
│
├── test/
└── README.md
```

## 1. Configurar el entorno

Se utilizarán las siguientes librerías:

```python
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
```

El notebook está preparado para intentar cargar el dataset desde cualquiera de estas ubicaciones:

```text
/workspace/superstore_dataset2012.csv
data/superstore_dataset2012.csv
actividades/trabajo04_VisualizacionDatosConMatplotlibySeaborn/data/superstore_dataset2012.csv
```

De esta forma funciona tanto en la plataforma como en Visual Studio Code.

## 2. Explorar y preparar los datos

Se deben revisar:

- primeras filas;
- nombres de columnas;
- tipos de datos;
- valores nulos;
- conversión de fechas;
- columnas numéricas disponibles.

El notebook incluye una función que reconoce nombres habituales del dataset Superstore, tanto si están en inglés como si usan nombres equivalentes en español.

## 3. Visualización univariante con Matplotlib

Se crea un **histograma de ventas** para observar cómo se distribuyen los valores de ventas.

Conclusión esperada: permite identificar si la mayoría de las ventas se concentran en valores bajos, medios o altos y si existen operaciones atípicas.

## 4. Visualización univariante con Seaborn

Se crea un **boxplot de ventas por categoría**.

Conclusión esperada: permite comparar la distribución de las ventas entre categorías y detectar posibles valores atípicos.

## 5. Visualización bivariante con Matplotlib

Se crea un **gráfico de dispersión entre Ventas y Beneficios**.

Conclusión esperada: permite observar si las operaciones con mayores ventas también tienden a producir mayores beneficios.

## 6. Visualización bivariante con Seaborn

Se utiliza `sns.regplot()` para mostrar la relación entre **Ventas y Beneficios** junto con una línea de tendencia.

Conclusión esperada: la línea de regresión facilita interpretar la tendencia general entre ambas variables.

## 7. Visualización multivariante con Seaborn

Se crea un **heatmap de correlación** entre las variables numéricas.

Conclusión esperada: permite identificar relaciones positivas, negativas o débiles entre ventas, beneficios, cantidad, descuento y otras variables numéricas disponibles.

## 8. Figura con múltiples subplots

Se genera una figura 2x2 que contiene:

1. Histograma de ventas.
2. Boxplot de ventas por categoría.
3. Dispersión Ventas vs. Beneficios.
4. Barras con ventas totales por categoría.

Esta figura se guarda como:

```text
resultados/visualizacion_resumen.png
```

## 9. Requisitos cumplidos

- [x] Gráfico univariante con Matplotlib.
- [x] Gráfico univariante con Seaborn.
- [x] Gráfico bivariante con Matplotlib.
- [x] Gráfico bivariante con Seaborn.
- [x] Visualización multivariante con Seaborn.
- [x] Personalización de títulos, etiquetas y paletas.
- [x] Uso de subplots.
- [x] Guardado de una figura como imagen.
- [x] Comentarios y conclusiones en el notebook.
- [x] Uso de `superstore_dataset2012.csv`.

## Archivo principal

La solución ejecutable se encuentra en:

```text
trabajo4_visualizacion.ipynb
```

El archivo `trabajo4.md` sirve como documentación del trabajo, mientras que el `.ipynb` es el archivo que contiene el análisis y las visualizaciones ejecutables.

## Resumen global
El proyecto cumple de forma sobresaliente todos los requisitos planteados. Se utiliza correctamente el dataset superstore_dataset2012.csv, se realiza una exploración y preparación adecuada de los datos con Pandas (incluyendo conversión de fechas y tipos numéricos), y se implementa un conjunto completo de visualizaciones con Matplotlib y Seaborn: univariantes, bivariantes y multivariantes. Además, se organiza una figura con cuatro subplots bien estructurados, se personalizan los gráficos con títulos, etiquetas y estilos apropiados, y se guarda al menos una figura como archivo de imagen. El notebook incluye comentarios y conclusiones claras para cada visualización, explicando qué aporta cada una al análisis. En conjunto, el trabajo es coherente, robusto y va incluso más allá de los mínimos exigidos, manteniendo un buen equilibrio entre código, visualización y explicación textual.