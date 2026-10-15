"""
Programa: Calculadora de calificaciones finales
Autor: Atl
Fecha: Octubre de 2026
Descripción: Solicita tres calificaciones, calcula el promedio final
y muestra la calificación final.
"""

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

# Bloque principal
if __name__=="__main__":
    # Entrada
    parciales = validar_calificacion("parciales")
    proyecto = validar_calificacion("proyecto")
    examen_final = validar_calificacion("examen final")

    # Proceso
    promedio_final = calcular_calificacion_final(parciales, proyecto, examen_final)

    # Salida
    print(f"Tu calificación final es: {promedio_final}")