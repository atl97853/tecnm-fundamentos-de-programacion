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

def obtener_calificacion_alfabetica(calificacion_numerica: int) -> str:
    """Convierte una calificación númerica de 0 a 100 en una calificación alfabética."""
    if 90 <= calificacion_numerica <= 100:
        return "A"
    elif 80 <= calificacion_numerica <= 89:
        return "B"
    elif 70 <= calificacion_numerica <= 79:
        return "C"
    elif 60 <= calificacion_numerica <= 69:
        return "D"
    else:
        return "F"

def main() -> None:
    """Solicita una calificación numérica y muestra su equivalente alfabético."""
    # Entrada
    calificacion_numerica = validar_calificacion()
    
    # Proceso
    calificacion_alfabetica = obtener_calificacion_alfabetica(calificacion_numerica)

    # Salida
    print(
        f"Tu calificación de {calificacion_numerica} equivale "
        f"a la letra {calificacion_alfabetica}."
    )   

# Bloque principal
if __name__ == "__main__":
    main()