# ============================================================
# Actividad 3: Programas Básicos en Python
# ============================================================
#
# Objetivo
# Desarrollar programas básicos para practicar variables,
# entrada de datos, operaciones aritméticas y salida de
# información.
#
# Descripción
# Resolver los ejercicios en Python con el editor de preferencia.
# Se recomienda Visual Studio Code por su integración con
# Python y Git.
# ============================================================


# ------------------------------------------------------------
# 01 · Cálculo del área de un rectángulo
# Desarrolla un programa que permita calcular el área de un 
# rectángulo a partir de los datos ingresados por el usuario.
# ------------------------------------------------------------
def area_rectangulo(ancho: float, largo: float) -> float:
    """Calcula el área de un rectángulo.

    Args:
        ancho: Medida del ancho del rectángulo.
        largo: Medida del largo del rectángulo.

    Returns:
        El área del rectángulo en unidades cuadradas.
    """
    return ancho * largo

# ------------------------------------------------------------
# 01 · Cálculo del promedio
# Desarrolla un programa que calcule el promedio de tres números 
# ingresados por el usuario.
# ------------------------------------------------------------
def calcular_promedio(
        primer_numero: float,
        segundo_numero: float,
        tercer_numero: float,
    ) -> float:
    """Calcula el promedio aritmético de tres números.

    Args:
        primer_numero: Primer número que se incluirá en el promedio.
        segundo_numero: Segundo número que se incluirá en el promedio.
        tercer_numero: Tercer número que se incluirá en el promedio.

    Returns:
        El promedio aritmético de los tres números.
    """
    return (primer_numero + segundo_numero + tercer_numero) / 3