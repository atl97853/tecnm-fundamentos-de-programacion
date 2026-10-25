"""
Programa: Conteo de números
Autor: Atl
Fecha: Octubre, 2026
Descripción: Solicita números enteros hasta que el usuario ingrese 'q'
y muestra cuántos son positivos, negativos o iguales a cero.
"""

def solicitar_numeros() -> list[int]:
    """Solicita números enteros hasta que el usuario ingrese 'q'."""
    return []

def contar_numeros_por_signo(lista_numeros: list[int]) -> tuple[int, int, int]:
    """Cuenta los números positivos, negativos e iguales a cero.

    Returns:
        Tupla con las cantidades de positivos, negativos y ceros,
        en ese orden.
    """
    return 0, 0, 0

def main() -> None:
    """Solicita números enteros y muestra sus conteos por signo."""
    # Entrada
    lista_numeros = solicitar_numeros()

    # Proceso
    positivos, negativos, ceros = contar_numeros_por_signo(lista_numeros)

    # Salida
    print(f"Números mayores que cero: {positivos}")
    print(f"Números menores que cero: {negativos}")
    print(f"Números iguales a cero: {ceros}")


if __name__ == "__main__":
    main()