"""
Programa: Calculadora de calificaciones finales
Autor: Atl
Fecha: Octubre, 2026
Descripción: Solicita tres calificaciones, calcula el promedio final
y muestra la calificación final.
"""

# Constantes
PORCENTAJE_PARCIALES = 40
PORCENTAJE_PROYECTO = 30
PORCENTAJE_EXAMEN_FINAL = 30

def validar_calificacion(evaluacion: str) -> int:
    """Solicita una calificación hasta obtener un número entero entre 0 y 100.

    Args:
        evaluacion: Nombre de la evaluación cuya calificación se solicita.

    Returns:
        Calificación validada, número entero entre 0 y 100, ambos incluidos.
    """
    while True:
        try: 
            calificacion = int(
                input(f"Ingresa la calificación de {evaluacion} (0-100): ")
            )        
        except ValueError:
            print("Por favor, ingresa una calificación válida.")
            continue

        if 0 <= calificacion <= 100:
            return calificacion
        else:
            print("La calificación debe de estar entre 0 y 100.")

def calcular_calificacion_final(parciales: int, proyecto:int , examen_final:int) -> int:
    """Calcula la calificación final mediante una suma ponderada.

    Args:
        parciales: Calificación de los exámenes parciales.
        proyecto: Calificación del proyecto.
        examen_final: Calificación del examen final.

    Returns:
        Calificación final entera, obtenida al truncar los decimales
        de la suma de los aportes ponderados.
    """
    aporte_parciales = (parciales * PORCENTAJE_PARCIALES) / 100
    aporte_proyecto = (proyecto * PORCENTAJE_PROYECTO) / 100
    aporte_examen_final = (examen_final * PORCENTAJE_EXAMEN_FINAL) / 100

    return int(
            aporte_parciales + aporte_proyecto + aporte_examen_final
        )

# Bloque principal
if __name__ == "__main__":
    # Entrada
    parciales = validar_calificacion("parciales")
    proyecto = validar_calificacion("proyecto")
    examen_final = validar_calificacion("examen final")

    # Proceso
    promedio_final = calcular_calificacion_final(parciales, proyecto, examen_final)

    # Salida
    print(f"Tu calificación final es: {promedio_final}")