"""
Programa: Calculadora básica con menú
Autor: Atl
Fecha: Octubre, 2026
Descripción: Calculadora básica que solicita dos números y una operación
aritmética, muestra el resultado y permite repetir hasta que
el usuario presione 'q' para salir.
"""

import re

def solicitar_numero(mensaje: str) -> float:
    """Solicita un número hasta que el usuario ingrese uno válido."""
    while True: 
        try: 
            return float(input(mensaje))
        except ValueError:
            print("Por favor, ingresa un número válido.")

def seleccionar_operacion() -> str:
    """Solicita y devuelve un símbolo de operación válido."""
    while True: 
        operacion = input("Elige una operación ('+', '-', '*', '/'): ").strip()
        patron = r"^[+*/-]$"

        if re.fullmatch(patron, operacion):
            return operacion
        else: 
            print("Operación no válida. Ingresa +, -, * o /.")

def calculadora(primer_numero: int, segundo_numero: int, operacion: str) -> float:
    """Calcula el resultado de la operación indicada."""
    match operacion:
        case "+":
            return primer_numero + segundo_numero
        case "-":
            return primer_numero - segundo_numero
        case "*":
            return primer_numero * segundo_numero
        case "/":
            return primer_numero / segundo_numero

def main() -> None:
    """Ejecuta la calculadora hasta que el usuario decida salir presionando 'q'."""

    while True: 
        # Entrada
        primer_numero = solicitar_numero("Ingresa tu primer número: ")
        operacion = seleccionar_operacion()
        segundo_numero = solicitar_numero("Ingresa tu segundo número: ")

        # Proceso
        try: 
            resultado = calculadora(primer_numero, segundo_numero, operacion)
        except ZeroDivisionError:
            print("No se puede dividir entre cero. Intenta de nuevo.")
            continue

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