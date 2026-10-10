# ============================================================
# Actividad 3: Programas Básicos en Python
# ============================================================

# 1. Área de un rectángulo
def area_rectangulo(ancho: float, largo: float) -> float:
    """Calcula el área de un rectángulo.

    Args:
        ancho: Medida del ancho del rectángulo.
        largo: Medida del largo del rectángulo.

    Returns:
        El área del rectángulo en unidades cuadradas.
    """
    return ancho * largo

# 2. Promedio de tres números
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

# 3. Índice de masa corporal
def indice_masa_corporal(peso_kg: float, altura_metros: float) -> float:
    """Calcula el IMC a partir del peso y la altura.

    Args:
        peso_kg: Peso de la persona en kilogramos.
        altura_metros: Altura de la persona en metros.

    Returns:
        El índice de masa corporal en kg/m².
    """
    return peso_kg / (altura_metros ** 2)

# 4. Salario neto mensual
def salario_neto(
        salario_bruto_mensual: float,
        porcentaje_impuestos: float,
        deducciones_adicionales: float,
    ) -> float:
    """Calcula el salario neto mensual después de impuestos y deducciones.

    Args:
        salario_bruto_mensual: Salario mensual antes de descuentos.
        porcentaje_impuestos: Porcentaje del salario destinado a impuestos;
            por ejemplo, 10 representa el 10 %.
        deducciones_adicionales: Importe de otros descuentos mensuales.

    Returns:
        Salario mensual restante después de todos los descuentos.
    """
    monto_impuestos = salario_bruto_mensual * (porcentaje_impuestos / 100)
    return salario_bruto_mensual - monto_impuestos - deducciones_adicionales