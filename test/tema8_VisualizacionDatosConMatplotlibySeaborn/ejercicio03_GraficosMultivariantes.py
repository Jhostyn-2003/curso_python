# Ejercicio 03: Gráficos Multivariantes
"""
Gráficos multivariantes
Objetivo
En este reto, se desarrollan gráficos de dispersión multivariantes utilizando Matplotlib para visualizar la relación entre cuatro variables. El objetivo es crear gráficos que incorporen colores y tamaños para representar información adicional, lo que resulta fundamental en el análisis de datos complejos, donde identificar patrones y correlaciones es clave.

Contexto
Este ejercicio será evaluado haciendo uso de Inteligencia Artificial.

Instrucciones
Crea un gráfico de dispersión multivariante utilizando Matplotlib para visualizar la relación entre cuatro variables. Genera un conjunto de datos aleatorios para las variables X, Y, color y tamaño. El gráfico debe seguir las siguientes especificaciones:

1.- Generación de datos:

Usa numpy para generar 200 puntos de datos para las variables X e Y con valores aleatorios entre 0 y 10.
La tercera variable debe mapearse a colores utilizando valores aleatorios entre 0 y 100.
La cuarta variable debe ser utilizada para el tamaño de los puntos, con valores aleatorios multiplicados por 200 para que los tamaños sean visibles.
2.- Configuración del gráfico de dispersión:

Usa plt.scatter() para crear el gráfico de dispersión.
Configura el color de los puntos mapeado a la tercera variable utilizando la paleta de colores plasma.
Ajusta el tamaño de los puntos mapeado a la cuarta variable y establece una transparencia (alpha) de 0.6 para mejorar la visibilidad.
3.- Etiquetas y título:

Añade un título descriptivo al gráfico, y etiquetas para los ejes X e Y.
4.- Barra de colores:

Añade una barra de colores que represente la escala de la tercera variable.
5.- Visualización:

Muestra el gráfico.
"""
import numpy as np
import matplotlib.pyplot as plt

# 1. Generación de datos
rng = np.random.default_rng(seed=42)

x = rng.uniform(0, 10, 200)
y = rng.uniform(0, 10, 200)

# Tercera variable: controla el color
colores = rng.uniform(0, 100, 200)

# Cuarta variable: controla el tamaño de los puntos
tamanos = rng.random(200) * 200

# 2. Crear el gráfico de dispersión multivariante
grafico = plt.scatter(
    x,
    y,
    c=colores,
    s=tamanos,
    cmap='plasma',
    alpha=0.6
)

# 3. Añadir título y etiquetas
plt.title('Gráfico de dispersión multivariante')
plt.xlabel('Variable X')
plt.ylabel('Variable Y')

# 4. Añadir barra de colores
barra_color = plt.colorbar(grafico)
barra_color.set_label('Variable de color')

# 5. Mostrar el gráfico
plt.show()
