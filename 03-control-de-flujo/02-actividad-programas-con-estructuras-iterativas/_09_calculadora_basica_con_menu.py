"""
Programa: Calculadora básica con menú
Autor: Atl
Fecha: Octubre, 2026
Descripción: Calculadora básica que solicita dos números y una operación
aritmética, muestra el resultado y permite repetir hasta que
el usuario presione 'q' para salir.
"""

def solicitar_numero() -> float:
    return 0

def seleccionar_operacion() -> str:
    return " "

def calculadora(primer_numero, segundo_numero, operacion) -> float:
    return 0

def main() -> None:
    """Ejecuta la calculadora hasta que el usuario decida salir presionando 'q'."""

    while True: 
        # Entrada
        primer_numero = solicitar_numero()
        segundo_numero = solicitar_numero()
        operacion = seleccionar_operacion()

        # Proceso
        resultado = calculadora(primer_numero, segundo_numero, operacion)

        # Salida
        print(
            f"Resultado: {primer_numero} {operacion} "
            f"{segundo_numero} = {resultado}"
        )

        salir = input("Presiona Enter para continuar o 'q' para salir: ").strip().lower()
        if salir == "q":
            break

if __name__ == "__main__":
    main()