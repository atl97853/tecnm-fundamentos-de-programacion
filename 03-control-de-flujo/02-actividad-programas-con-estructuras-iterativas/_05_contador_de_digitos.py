"""
Programa: Contador de dígitos
Autor: Atl
Fecha: Solicita un número entero, cuenta los dígitos de su
representación decimal sin incluir el signo y muestra la cantidad.
"""

def calcular_valor_absoluto(numero: int) -> int:
    """Devuelve el valor absoluto de un número entero."""
    if numero < 0:
        return -numero

    return numero

def solicitar_entero() -> int:
    """Solicita un número entero y repite la petición hasta obtenerlo.

    Si el número ingresado es negativo, lo convierte en positivo antes
    de devolverlo.
    """
    return 0

def contar_digitos(numero: int) -> int:
    """Cuenta los dígitos de un entero en su representación decimal."""
    return 0

def main() -> None:
    """Solicita un entero y muestra cuántos dígitos tiene."""
    # Entrada
    numero = solicitar_entero()

    # Proceso
    cantidad_digitos = contar_digitos(numero)

    # Salida
    print(f"Cantidad de dígitos de {numero}: {cantidad_digitos}.")


if __name__ == "__main__":
    main()