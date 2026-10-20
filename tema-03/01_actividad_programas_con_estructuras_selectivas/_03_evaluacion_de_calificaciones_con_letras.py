"""
Programa: Evaluación de calificaciones con letas
Autor: Atl
Fecha: Octubre, 2026
Descripción: Solicita y valida una calificación numérica y la convierte
en su equivalente alfabético según los rangos establecidos.
"""

# Bloque principal
if __name__ == "__main__":
    # Entrada
    calificacion_numerica = validar_calificacion()
    
    # Proceso
    calificacion_alfabetica = obtener_calificacion_alfabetica(calificacion_numerica)

    # Salida
    print(f"Tu calificación alfabética es: {calificacion_alfabetica}")