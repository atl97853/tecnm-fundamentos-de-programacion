"""
Generar una secuencia aritmética (con do-while simulado)
Autor: Atl
Fecha: Octubre, 2026
Descripción: Solicita el primer término, la diferencia común y un valor
máximo; después muestra la secuencia aritmética hasta ese valor mediante
un bucle do-while simulado.
"""

def solicitar_entero(mensaje: str) -> int:
    """Solicita un intento y repite la petición hasta obtener uno válido."""
    while True: 
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada no válida. Ingresa un número entero.")

def mostrar_secuencia_aritmetica(primer_termino: int, diferencia_comun: int, valor_maximo: int) -> None:
    """Muestra los términos de la secuencia hasta el valor máximo."""
    pass  # Pendiente de implementar


def main() -> None:
    """Solicita los datos y muestra la secuencia aritmética."""

    # Entrada
    primer_termino = solicitar_entero("Ingresa el primer término: ")
    diferencia_comun = solicitar_entero("Ingresa la diferencia común: ")

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