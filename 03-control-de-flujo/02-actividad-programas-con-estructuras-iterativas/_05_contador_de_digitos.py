"""
Programa: Contador de dígitos
Autor: Atl
Fecha: Octubre, 2026 
Descripción: Solicita un número entero, cuenta los dígitos de su
representación decimal sin incluir el signo y muestra la cantidad.
"""

def valor_absoluto(numero: int) -> int:
    """Convierte un número entero a su valor absoluto."""
    if numero < 0:
        return -numero

    return numero

def solicitar_entero() -> int:
    """Solicita un número entero y repite la petición hasta obtenerlo.

    Si el número ingresado es negativo, lo convierte en positivo antes
    de devolverlo.
    """
    while True:
        try:
            numero = int(input("Ingresa un número: "))
        except ValueError:
            print("Por favor, ingresa un número valido.")
            continue

        return valor_absoluto(numero)

def contar_digitos(numero: int) -> int:
    """Cuenta los dígitos de un entero en su representación decimal."""
    if numero == 0:
        return 1

    conteo_digitos = 0 # variable de conteo

    while numero > 0:
        conteo_digitos += 1
        numero = numero / 10 # elimina el último dígito decimal

    return conteo_digitos

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