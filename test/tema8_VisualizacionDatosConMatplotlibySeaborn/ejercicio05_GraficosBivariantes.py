# Ejercicio 05 - Gráficos Bivariantes
"""
Gráficos bivariantes
Objetivo
En este ejercicio, usarás Seaborn para visualizar la relación entre el total de la cuenta y la propina, diferenciando por sexo y superponiendo una línea de regresión.

Contexto
Este ejercicio será evaluado utilizando inteligencia artificial.

Instrucciones
Utilizando Seaborn, crea una visualización bivariante que analice la relación entre dos variables numéricas del conjunto de datos tips. Personaliza el gráfico según los siguientes requisitos:

Carga el conjunto de datos tips utilizando sns.load_dataset.
Configura el estilo del gráfico a  whitegrid.
Crea un gráfico de dispersión entre las variables total_bill y tip.
Usa una paleta personalizada con el parámetro palette configurado como coolwarm.
Diferencia los puntos en función del sexo con el parámetro hue='sex'.
Ajusta el nivel de transparencia de los puntos con alpha=0.6 para mejorar la visualización en datos densos.
Añade un título descriptivo y etiquetas claras para ambos ejes.
Superpón una línea de regresión utilizando sns.regplot() para observar tendencias entre las variables, ocultando los puntos de dispersión con scatter=False.
Muestra el gráfico combinando ambas visualizaciones en un solo espacio.
"""

import seaborn as sns
import matplotlib.pyplot as plt

# 1. Cargar el conjunto de datos tips
tips = sns.load_dataset('tips')

# 2. Configurar el estilo del gráfico
sns.set_style('whitegrid')

# 3, 4, 5 y 6. Crear el gráfico de dispersión
sns.scatterplot(
    data=tips,
    x='total_bill',
    y='tip',
    hue='sex',
    palette='coolwarm',
    alpha=0.6
)

# 8. Superponer una línea de regresión
sns.regplot(
    data=tips,
    x='total_bill',
    y='tip',
    scatter=False
)

# 7. Añadir título y etiquetas
plt.title('Relación entre el total de la cuenta y la propina')
plt.xlabel('Total de la cuenta')
plt.ylabel('Propina')

# 9. Mostrar el gráfico
plt.show()
