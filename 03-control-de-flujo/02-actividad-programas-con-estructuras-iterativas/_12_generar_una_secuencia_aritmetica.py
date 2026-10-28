"""
Generar una secuencia aritmética (con do-while simulado)
Autor: Atl
Fecha: Octubre, 2026
Descripción: Solicita el primer término, la diferencia común y un valor
máximo; después muestra la secuencia aritmética hasta ese valor mediante
un bucle do-while simulado.
"""

def solicitar_entero(mensaje: str) -> int:
    """Solicita un número entero y repite la petición hasta obtener uno válido."""
    while True: 
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada no válida. Ingresa un número entero.")

def calcular_siguiente_termino(termino_actual: int, diferencia_comun: int) -> int:
    """Devuelve el siguiente término de la secuencia aritmética."""
    return termino_actual + diferencia_comun

def mostrar_secuencia_aritmetica(primer_termino: int, diferencia_comun: int, valor_maximo: int) -> None:
    """Muestra los términos de la secuencia hasta el valor máximo."""
    numero_actual = primer_termino

    while True: 
        print(numero_actual)
        numero_actual = calcular_siguiente_termino(numero_actual, diferencia_comun)

        # El término actual ya se imprimió. Si el siguiente supera el máximo,
        # termina el ciclo; si es menor o igual, se imprimirá en la próxima vuelta.
        if numero_actual > valor_maximo:
            break

def main() -> None:
    """Solicita los datos y muestra la secuencia aritmética."""

    # Entrada
    primer_termino = solicitar_entero("Ingresa el primer término: ")

    while True:
        diferencia_comun = solicitar_entero("Ingresa la diferencia común: ")

        if diferencia_comun > 0:
            break
        else:
            print("La diferencia común debe ser mayor que cero. Intenta de nuevo.")

    while True: 
        valor_maximo = solicitar_entero("Ingresa el valor máximo: ")

        if valor_maximo >= primer_termino:
            break
        else:
            print(
                f"El valor máximo debe ser al menos {primer_termino}. "
                "Intenta de nuevo."
            )

    # Proceso y salida
    mostrar_secuencia_aritmetica(
        primer_termino, diferencia_comun, valor_maximo
    )

if __name__ == "__main__":
    main()