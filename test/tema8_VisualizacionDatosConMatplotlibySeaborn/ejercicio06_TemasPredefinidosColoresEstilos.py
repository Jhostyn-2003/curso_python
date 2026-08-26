# Ejercicio 06 - Temas Predefinidos, Colores y Estilos
"""
Temas predefinidos, colores y estilos
Objetivo
Crea un gráfico de barras en Seaborn con tema, paleta y personalizaciones avanzadas, incluyendo eliminación de bordes y ajuste de leyenda.

Contexto
Este ejercicio será evaluado utilizando inteligencia artificial.

Instrucciones
Utilizando Seaborn en Python, crea un script que genere un gráfico de barras (barplot) con datos ficticios. El gráfico debe cumplir los siguientes requisitos:

Crea un DataFrame con datos ficticios:
El DataFrame debe tener dos columnas:
Categoría, que contiene las categorías A, B, C, D.
Valor, que contiene los valores numéricos 10, 15, 7, 12.
Aplica el tema predefinido whitegrid al gráfico.
Utiliza la paleta de colores pastel para las barras.
Crea un gráfico de barras:
Usa la función sns.barplot() para graficar los datos del DataFrame:
Eje x: la columna Categoría.
Eje y: la columna Valor.
Asigna la columna Categoría al parámetro hue para garantizar compatibilidad con futuras versiones de Seaborn.
Establece la paleta de colores pastel mediante el argumento palette.
Personaliza el título del gráfico:
El título debe ser: Gráfico de barras personalizado.
Debe tener:
Tamaño de fuente de 16.
Color azul.
Negrita (bold).
Personaliza las etiquetas de los ejes:
Cambia la etiqueta del eje x a Categorías y la del eje y a Valores.
Ambas etiquetas deben tener:
Tamaño de fuente de 12.
Color gris oscuro.
Elimina bordes específicos del gráfico:
Usa sns.despine() para eliminar los bordes izquierdo y derecho del gráfico.
Muestra el gráfico resultante.
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Crear un DataFrame con datos ficticios
df = pd.DataFrame({
    'Categoría': ['A', 'B', 'C', 'D'],
    'Valor': [10, 15, 7, 12]
})

# Aplicar el tema whitegrid
sns.set_style('whitegrid')

# Crear el gráfico de barras
sns.barplot(
    data=df,
    x='Categoría',
    y='Valor',
    hue='Categoría',
    palette='pastel'
)

# Personalizar el título
plt.title(
    'Gráfico de barras personalizado',
    fontsize=16,
    color='blue',
    fontweight='bold'
)

# Personalizar las etiquetas de los ejes
plt.xlabel(
    'Categorías',
    fontsize=12,
    color='darkgray'
)

plt.ylabel(
    'Valores',
    fontsize=12,
    color='darkgray'
)

# Eliminar los bordes izquierdo y derecho
sns.despine(
    left=True,
    right=True
)

# Mostrar el gráfico
plt.show()
