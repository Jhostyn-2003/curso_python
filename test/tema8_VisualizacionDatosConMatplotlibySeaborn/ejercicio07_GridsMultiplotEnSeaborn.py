# Ejercicio 07 - Grids Multiplot en Seaborn
"""
Grids Multiplot en Seaborn
Objetivo
En este ejercicio, vas a crear una visualización utilizando Seaborn que demuestre tu habilidad para trabajar con grids multiplot y personalizar gráficos. Tu tarea es utilizar el objeto FacetGrid para analizar un conjunto de datos por subgrupos categóricos y representar las distribuciones de una variable numérica en múltiples facetas.

Contexto
Este ejercicio será evaluado utilizando inteligencia artificial.

Instrucciones
Cargar el conjunto de datos: Utiliza el conjunto de datos penguins de Seaborn. Este conjunto de datos contiene información sobre características físicas de pingüinos, como el largo de su aleta, su peso y su especie.
Crear una cuadrícula de facetas:
Usa FacetGrid para crear una cuadrícula que segmente los datos por la especie (species) en las columnas y por el sexo (sex) en las filas.
Dentro de cada faceta, representa la relación entre el largo de la aleta (flipper_length_mm) y el peso corporal (body_mass_g) utilizando un gráfico de dispersión (scatterplot).
Personalización:
Añade una variable adicional hue basada en la isla de origen (island) para diferenciar los datos dentro de cada faceta.
Asegúrate de incluir una leyenda para identificar los subgrupos de hue.
Ajusta el tamaño de las facetas y el espacio entre ellas para asegurar una visualización clara y legible.
Añade títulos y etiquetas a los ejes para mejorar la interpretación de los gráficos.
Ajusta los límites del eje x y del eje y para un rango consistente en todas las facetas.
Mostrar la visualización: Configura y muestra la visualización completa.
"""
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el conjunto de datos penguins
penguins = sns.load_dataset('penguins')

# Eliminar filas con valores nulos en las columnas utilizadas
penguins = penguins.dropna(
    subset=[
        'species',
        'sex',
        'island',
        'flipper_length_mm',
        'body_mass_g'
    ]
)

# Crear la cuadrícula de facetas
g = sns.FacetGrid(
    penguins,
    col='species',
    row='sex',
    hue='island',
    height=4,
    aspect=1.2
)

# Crear gráfico de dispersión en cada faceta
g.map_dataframe(
    sns.scatterplot,
    x='flipper_length_mm',
    y='body_mass_g'
)

# Añadir leyenda
g.add_legend(title='Isla')

# Añadir etiquetas a los ejes
g.set_axis_labels(
    'Longitud de la aleta (mm)',
    'Peso corporal (g)'
)

# Añadir títulos a las facetas
g.set_titles(
    row_template='Sexo: {row_name}',
    col_template='Especie: {col_name}'
)

# Ajustar límites de los ejes
g.set(
    xlim=(165, 235),
    ylim=(2500, 6500)
)

# Ajustar espacio entre las facetas
g.figure.subplots_adjust(
    wspace=0.15,
    hspace=0.20
)

# Título general
g.figure.suptitle(
    'Relación entre longitud de aleta y peso corporal de los pingüinos',
    y=1.03
)

# Mostrar la visualización
plt.show()

