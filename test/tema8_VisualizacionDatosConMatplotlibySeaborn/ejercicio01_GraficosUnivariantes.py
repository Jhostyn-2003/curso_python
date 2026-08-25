# Ejercicio 01: Gráficos Univariantes
"""
Gráficos univariantes
Objetivo
Este ejercicio te guiará en la creación de un histograma utilizando Matplotlib, permitiéndote visualizar la distribución de un conjunto de datos generado aleatoriamente y aplicando técnicas de personalización para mejorar la claridad visual.

Contexto
Este ejercicio será evaluado haciendo uso de Inteligencia Artificial.

Instrucciones
Crea un histograma utilizando Matplotlib para visualizar la distribución de un conjunto de datos generado aleatoriamente. Debes seguir las siguientes especificaciones:

1.- Generación de datos:

Usa numpy para crear un conjunto de 1500 datos con distribución normal (media=5, desviación estándar=2).
2.- Configuración del histograma:

Utiliza plt.hist() para crear el histograma.
Establece el número de intervalos (bins) en 40.
Configura el color de las barras a verde con una transparencia (alpha) de 0.5.
Añade bordes rojos a las barras para mejorar la claridad visual.
3.- Añadir información al gráfico:

Incluye un título descriptivo, y etiquetas para los ejes x e y.
4.- Visualización:

Muestra el gráfico.
"""
import numpy as np
import matplotlib.pyplot as plt

# 1. Generación de datos
datos = np.random.normal(
    loc=5,
    scale=2,
    size=1500
)

# 2. Crear el histograma
plt.hist(
    datos,
    bins=40,
    color='green',
    alpha=0.5,
    edgecolor='red'
)

# 3. Añadir información al gráfico
plt.title('Distribución de datos con distribución normal')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# 4. Mostrar el gráfico
plt.show()
