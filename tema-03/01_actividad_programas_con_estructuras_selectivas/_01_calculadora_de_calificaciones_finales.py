"""
Programa: Calculadora de calificaciones finales
Autor: Atl
Fecha: Octubre de 2026
Descripción: Solicita tres calificaciones, calcula el promedio final
y muestra la calificación final.
"""

# Bloque principal
if __name__=="__main__":
    # Entrada
    parciales = validar_calificacion()
    proyecto = validar_calificacion()
    examen_final = validar_calificacion()

    # Proceso
    promedio_final = calcular_calificacion_final(parciales, proyecto, examen_final)

    # Salida
    print(f"Tu calificación final es: {promedio_final}")