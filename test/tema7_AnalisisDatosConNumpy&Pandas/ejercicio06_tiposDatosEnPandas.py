# Ejercicio 06: Tipos de datos en Pandas
"""
Ejercicio tipos de datos en Pandas
Objetivo
Verificación y conversión de tipos de datos en un DataFrame de Pandas

Instrucciones
Crea un DataFrame con las siguientes columnas: 'edad' (valores enteros), 'altura' (valores decimales), 'nombre' (texto) y 'activo' (booleanos). Luego realiza las siguientes tareas:

Verifica y muestra los tipos de datos de todas las columnas usando el atributo dtypes
Convierte la columna 'edad' a tipo float64
Convierte la columna 'altura' a tipo int64
Convierte la columna 'nombre' a tipo category
Muestra nuevamente los tipos de datos para verificar los cambios
Calcula y muestra el uso de memoria del DataFrame antes y después de las conversiones usando memory_usage(deep=True)

"""
import pandas as pd
import numpy as np

# Crear un DataFrame con diferentes tipos de datos
df = pd.DataFrame({
    'edad': [25, 30, 35, 40, 45],
    'altura': [1.75, 1.80, 1.65, 1.90, 1.70],
    'nombre': ['Ana', 'Juan', 'María', 'Carlos', 'Laura'],
    'activo': [True, False, True, True, False]
})

# 1. Verificar y mostrar los tipos de datos iniciales
# TODO: Imprimir los tipos de datos iniciales
print("Tipos de datos iniciales:")
print(df.dtypes)

# Calcular el uso de memoria antes de las conversiones
# TODO: Calcular y mostrar el uso de memoria antes de las conversiones
memoria_antes = df.memory_usage(deep=True).sum()

print("\nUso de memoria antes de las conversiones:")
print(memoria_antes, "bytes")

# 2. Convertir la columna 'edad' a tipo float64
# TODO: Convertir la columna 'edad' a tipo float64
df['edad'] = df['edad'].astype('float64')

# 3. Convertir la columna 'altura' a tipo int64
# TODO: Convertir la columna 'altura' a tipo int64
df['altura'] = df['altura'].astype('int64')

# 4. Convertir la columna 'nombre' a tipo category
# TODO: Convertir la columna 'nombre' a tipo category
df['nombre'] = df['nombre'].astype('category')

# 5. Mostrar los tipos de datos después de las conversiones
# TODO: Imprimir los tipos de datos después de las conversiones
print("\nTipos de datos después de las conversiones:")
print(df.dtypes)

# 6. Calcular y mostrar el uso de memoria después de las conversiones
# TODO: Calcular y mostrar el uso de memoria después de las conversiones
memoria_despues = df.memory_usage(deep=True).sum()

print("\nUso de memoria después de las conversiones:")
print(memoria_despues, "bytes")

# Mostrar la diferencia de memoria
# TODO: Imprimir la diferencia de memoria
diferencia_memoria = memoria_antes - memoria_despues

print("\nDiferencia de memoria:")
print(diferencia_memoria, "bytes")

# Mostrar el DataFrame con los tipos de datos convertidos
# TODO: Imprimir el DataFrame con tipos de datos convertidos
print("\nDataFrame con tipos de datos convertidos:")
print(df)