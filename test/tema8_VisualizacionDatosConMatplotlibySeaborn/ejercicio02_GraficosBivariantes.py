# Ejercicio 02: Gráficos Bivariantes
"""
Gráficos bivariantes
Objetivo
El reto consiste en crear un gráfico de dispersión utilizando Matplotlib que visualice la relación entre dos variables numéricas generadas aleatoriamente. Además, se debe calcular y mostrar una línea de regresión que indique la tendencia de los datos, personalizando el gráfico con colores, etiquetas para los ejes, un título descriptivo y cuadrícula para mejorar la claridad visual.

Contexto
Este ejercicio será evaluado haciendo uso de Inteligencia Artificial.

Instrucciones
1.- Generación de los datos:

Crea dos conjuntos de datos con numpy. El primer conjunto x contendrá 100 valores aleatorios entre 0 y 50, y el segundo conjunto y tendrá una relación lineal con x (por ejemplo, y = 2.5 * x + ruido, donde el ruido es una pequeña variación aleatoria para simular datos reales). Se podría ver así:
x = rng.uniform(0, 50, 100)
ruido = rng.normal(0, 10, 100)
y = 2.5 * x + ruido
2.- Calcular la línea de regresión:

Utiliza numpy.polyfit para calcular la línea de regresión lineal que mejor se ajuste a los datos.
3.- Configuración del gráfico de dispersión:

Usa plt.scatter() para crear el gráfico de dispersión.
Configura el color de los puntos a púrpura (purple) y ajusta el tamaño de los puntos a 50 para mejorar la visualización.
Añade una línea de regresión con plt.plot() en color verde (green).
Incluye una cuadrícula para mejorar la interpretación del gráfico.
4.- Etiquetas y título:

Añade un título descriptivo para el gráfico, además de etiquetas para los ejes X e Y.
5.- Visualización:

Muestra el gráfico utilizando plt.show().
"""
import numpy as np
import matplotlib.pyplot as plt

# 1. Generación de los datos
rng = np.random.default_rng(seed=42)

x = rng.uniform(0, 50, 100)
ruido = rng.normal(0, 10, 100)
y = 2.5 * x + ruido

# 2. Calcular la línea de regresión
pendiente, intercepto = np.polyfit(x, y, 1)

y_regresion = pendiente * x + intercepto

# 3. Crear el gráfico de dispersión
plt.scatter(
    x,
    y,
    color='purple',
    s=50,
    label='Datos'
)

# Añadir la línea de regresión
plt.plot(
    x,
    y_regresion,
    color='green',
    label='Línea de regresión'
)

# Añadir cuadrícula
plt.grid(True)

# 4. Añadir título y etiquetas
plt.title('Relación entre X e Y con línea de regresión')
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

# Mostrar leyenda
plt.legend()

# 5. Mostrar el gráfico
plt.show()