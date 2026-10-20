"""
Programa: Evaluación de calificaciones con letas
Autor: Atl
Fecha: Octubre, 2026
Descripción: Solicita y valida una calificación numérica y la convierte
en su equivalente alfabético según los rangos establecidos.
"""

def validar_calificacion() -> int:
    """Solicita una calificación hasta obtener un número entero entre 0 y 100."""
    while True:
        try:
            calificacion = int(
                input("Ingresa tu calificación (0-100): ")
            )
        except ValueError:
            print("Por favor, ingresa una calificación válida.")
            continue

        if 0 <= calificacion <= 100:
            return calificacion
        else:
            print("La calificación debe de estar entre 0 y 100.")

# Bloque principal
if __name__ == "__main__":
    # Entrada
    calificacion_numerica = validar_calificacion()
    
    # Proceso
    calificacion_alfabetica = obtener_calificacion_alfabetica(calificacion_numerica)

    # Salida
    print(f"Tu calificación alfabética es: {calificacion_alfabetica}")