# ============================================================
# ACTIVIDAD 3: Programas Básicos en Python
# ============================================================

# Variables constantes
TASA_IMPUESTO = 0.16

# ============================================================
# FUNCIONES: cada una recibe datos y devuelve un resultado.
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

# ============================================================
# INTERFAZ DE CONSOLA
# Solicita los datos de los cuatro ejercicios y muestra
# los resultados calculados por sus funciones.
# ============================================================
def main() -> None:
    """Ejecuta los cuatro ejercicios con datos ingresados por el usuario."""
    print("=== Actividad 3: Programas Básicos en Python ===")

    # 1. Área de un rectángulo
    print("\n1. Área de un rectángulo")
    ancho = float(input("Ancho: "))
    largo = float(input("Largo: "))
    print(f"Área: {area_rectangulo(ancho, largo):.2f} unidades²")

    # 2. Promedio de tres números
    print("\n2. Promedio de tres números")
    primer_numero = float(input("Primer número: "))
    segundo_numero = float(input("Segundo número: "))
    tercer_numero = float(input("Tercer número: "))
    promedio = calcular_promedio(primer_numero, segundo_numero, tercer_numero)
    print(f"Promedio: {promedio:.2f}")

    # 3. Índice de masa corporal
    print("\n3. Índice de masa corporal")
    peso_kg = float(input("Peso en kilogramos: "))
    altura_metros = float(input("Altura en metros: "))
    imc = indice_masa_corporal(peso_kg, altura_metros)
    print(f"IMC: {imc:.2f} kg/m²")

    # 4. Salario neto mensual
    print("\n4. Salario neto mensual")
    print(f"La tasa de impuesto actual es del: {TASA_IMPUESTO:.2F}%")
    salario_bruto_mensual = float(input("Salario bruto mensual: "))
    porcentaje_impuestos = TASA_IMPUESTO
    deducciones_adicionales = float(input("Deducciones adicionales: "))
    resultado = salario_neto(
        salario_bruto_mensual,
        porcentaje_impuestos,
        deducciones_adicionales,
    )
    print(f"Salario neto mensual: {resultado:.2f}")

# ============================================================
# PUNTO DE ENTRADA
# Inicia la interacción solo al ejecutar este archivo directamente.
# ============================================================
if __name__ == "__main__":
    main()

# ============================================================
# REFERENCIAS
# Lecturas para repasar los conceptos utilizados en esta actividad.
# ============================================================
# Docstrings:
# https://realpython.com/ref/best-practices/docstrings/
#
# Estilo de comentarios y docstrings:
# https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
#
# Uso de if __name__ == "__main__":
# https://realpython.com/if-name-main-python/#frequently-asked-questions
#
# Formato de texto con f-strings:
# https://www.geeksforgeeks.org/python/formatted-string-literals-f-strings-python/