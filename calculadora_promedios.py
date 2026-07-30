def ingresar_calificaciones():
    """
    Solicita al usuario nombres de materias y sus calificaciones.

    Retorna:
        materias: lista con los nombres de las materias.
        calificaciones: lista con las calificaciones ingresadas.
    """
    materias = []
    calificaciones = []

    while True:
        materia = input("\nIngrese el nombre de la materia: ").strip()

        # Validar que el nombre de la materia no esté vacío
        if materia == "":
            print("Error: el nombre de la materia no puede estar vacío.")
            continue

        # Validar que la calificación sea un número entre 0 y 10
        while True:
            try:
                calificacion = float(
                    input(f"Ingrese la calificación de {materia} (0 a 10): ")
                )

                if 0 <= calificacion <= 10:
                    break

                print("Error: la calificación debe estar entre 0 y 10.")

            except ValueError:
                print("Error: debe ingresar un valor numérico.")

        # Guardar los datos en listas separadas
        materias.append(materia)
        calificaciones.append(calificacion)

        # Preguntar si se desea continuar
        while True:
            continuar = input(
                "¿Desea ingresar otra materia? (s/n): "
            ).strip().lower()

            if continuar in ["s", "si", "sí"]:
                break

            if continuar in ["n", "no"]:
                return materias, calificaciones

            print("Respuesta no válida. Escriba 's' para continuar o 'n' para terminar.")


def calcular_promedio(calificaciones):
    """
    Calcula el promedio de una lista de calificaciones.

    Retorna:
        El promedio de las calificaciones.
    """
    if len(calificaciones) == 0:
        return 0

    suma_calificaciones = sum(calificaciones)
    promedio = suma_calificaciones / len(calificaciones)

    return promedio


def determinar_estado(calificaciones, umbral=5.0):
    """
    Determina los índices de las materias aprobadas y reprobadas.

    Parámetros:
        calificaciones: lista de calificaciones.
        umbral: nota mínima para aprobar. Por defecto es 5.0.

    Retorna:
        aprobadas: lista de índices de materias aprobadas.
        reprobadas: lista de índices de materias reprobadas.
    """
    aprobadas = []
    reprobadas = []

    for indice in range(len(calificaciones)):
        if calificaciones[indice] >= umbral:
            aprobadas.append(indice)
        else:
            reprobadas.append(indice)

    return aprobadas, reprobadas


def encontrar_extremos(calificaciones):
    """
    Encuentra los índices de la calificación más alta y más baja.

    Retorna:
        indice_mayor: índice de la calificación más alta.
        indice_menor: índice de la calificación más baja.
    """
    if len(calificaciones) == 0:
        return None, None

    indice_mayor = calificaciones.index(max(calificaciones))
    indice_menor = calificaciones.index(min(calificaciones))

    return indice_mayor, indice_menor


def main():
    """
    Función principal del programa.
    """
    print("=" * 50)
    print("       CALCULADORA DE PROMEDIOS ESCOLARES")
    print("=" * 50)

    materias, calificaciones = ingresar_calificaciones()

    # Manejar el caso en el que no se hayan ingresado materias
    if len(materias) == 0:
        print("\nNo se ingresó ninguna materia.")
        print("Gracias por utilizar la calculadora de promedios.")
        return

    promedio = calcular_promedio(calificaciones)

    indices_aprobadas, indices_reprobadas = determinar_estado(
        calificaciones,
        umbral=5.0
    )

    indice_mejor, indice_peor = encontrar_extremos(calificaciones)

    print("\n" + "=" * 50)
    print("  RESUMEN FINAL  ")
    print("=" * 50)

    print("\nMaterias y calificaciones:")

    for indice in range(len(materias)):
        print(
            f"{indice + 1}. {materias[indice]}: "
            f"{calificaciones[indice]:.2f}"
        )

    print(f"\nPromedio general: {promedio:.2f}")

    print("\nMaterias aprobadas:")

    if len(indices_aprobadas) > 0:
        for indice in indices_aprobadas:
            print(
                f"- {materias[indice]}: "
                f"{calificaciones[indice]:.2f}"
            )
    else:
        print("- No hay materias aprobadas.")

    print("\nMaterias reprobadas:")

    if len(indices_reprobadas) > 0:
        for indice in indices_reprobadas:
            print(
                f"- {materias[indice]}: "
                f"{calificaciones[indice]:.2f}"
            )
    else:
        print("- No hay materias reprobadas.")

    print(
        f"\nMateria con mejor calificación: "
        f"{materias[indice_mejor]} "
        f"({calificaciones[indice_mejor]:.2f})"
    )

    print(
        f"Materia con peor calificación: "
        f"{materias[indice_peor]} "
        f"({calificaciones[indice_peor]:.2f})"
    )

    print("\nGracias por utilizar la calculadora de promedios.")
    print("¡Hasta pronto!")


if __name__ == "__main__":
    main()