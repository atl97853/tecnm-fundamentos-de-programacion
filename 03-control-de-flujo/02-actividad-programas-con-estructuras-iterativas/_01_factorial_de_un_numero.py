"""
Programa: Cálculo del factorial
Autor: Atl
Fecha: Octubre de 2026
Descripción: Solicita un número entero no negativo, calcula su factorial
mediante un proceso iterativo y muestra el resultado en la terminal.
"""

def solicitar_entero_no_negativo() -> int:
    """Solicita un entero no negativo y repite la petición hasta obtenerlo."""
    raise NotImplementedError("Pendiente: solicitar y validar la entrada.")

def calcular_factorial_iterativo(numero: int) -> int:
    """Calcula el factorial de un entero no negativo mediante iteración."""
    raise NotImplementedError("Pendiente: implementar el cálculo iterativo.")

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