# Ejercicio 04 - Gráficos Univariantes
"""
Gráficos univariantes
Objetivo
En este ejercicio, crearás un histograma con Seaborn ajustando parámetros como bins y KDE, añadiendo etiquetas y un título al gráfico.

Contexto
Este ejercicio será evaluado utilizando inteligencia artificial.

Instrucciones
Utilizando la biblioteca Seaborn, crea un histograma para visualizar la distribución de la variable tip del conjunto de datos tips. Personaliza el histograma con los siguientes requisitos adicionales para hacerlo único.

Variable a graficar: Utiliza la variable tip.
Número de bins: Configura el histograma con 40 bins.
Visualización de densidad: Muestra la densidad en lugar de la frecuencia.
KDE: Superpón una curva KDE de color azul (color='blue').
Estilo general: Configura el estilo del gráfico con sns.set_style('darkgrid').
Etiquetas y título: Personaliza las etiquetas de los ejes y añade un título relevante para el gráfico.
"""

import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el conjunto de datos tips
tips = sns.load_dataset('tips')

# Configurar el estilo general
sns.set_style('darkgrid')

# Crear el histograma
sns.histplot(
    data=tips,
    x='tip',
    bins=40,
    stat='density',
    kde=False
)

# Superponer la curva KDE en color azul
sns.kdeplot(
    data=tips,
    x='tip',
    color='blue'
)

# Añadir etiquetas y título
plt.xlabel('Propina')
plt.ylabel('Densidad')
plt.title('Distribución de las propinas')

# Mostrar el gráfico
plt.show()

