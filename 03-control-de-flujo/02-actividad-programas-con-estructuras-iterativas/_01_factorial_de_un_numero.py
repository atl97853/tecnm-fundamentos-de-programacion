"""
Programa: Cálculo del factorial
Autor: Atl
Fecha: Octubre de 2026
Descripción: Solicita un número entero no negativo, calcula su factorial
mediante un proceso iterativo y muestra el resultado en la terminal.
"""

def solicitar_entero_no_negativo() -> int:
    """Solicita un entero no negativo y repite la petición hasta obtenerlo."""
    while True:
        try:
            numero = int(input("Ingresa un número entero mayor o igual a cero: "))
        except ValueError:
            print("Por favor, ingresa un número valido.")
            continue

        if numero >= 0:
            return numero
        print("Por favor, ingresa un numero entero mayor o igual a cero.")

def calcular_factorial_iterativo(numero: int) -> int:
    """Calcula el factorial de un entero no negativo."""
    producto = 1

    # Para 0 y 1, el rango está vacío y producto permanece en 1.
    for factor in range(2, numero + 1):
        producto = factor * producto

    return producto

def main() -> None:
    """Solicita un entero no negativo y muestra su factorial."""
    # Entrada
    numero = solicitar_entero_no_negativo()

    # Proceso
    factorial = calcular_factorial_iterativo(numero)

    # Salida
    print(f"El factorial de {numero} es {factorial}.")

if __name__ == "__main__":
    main()