"""
Programa: Conteo de números
Autor: Atl
Fecha: Octubre, 2026
Descripción: Solicita números enteros hasta que el usuario ingrese 'q'
y muestra cuántos son positivos, negativos o iguales a cero.
"""

def solicitar_numeros() -> list[int]:
    """Solicita números enteros hasta que el usuario ingrese 'q'."""
    lista_numeros: list[int] = []

    while True:
        entrada = input(
            "Ingresa un número entero (positivo, negativo o cero), "
            "o 'q' para terminar: "
        ).strip()

        if entrada.lower() == "q":
            return lista_numeros

        try:
            numero = int(entrada)
        except ValueError:
            print("Entrada no válida. Ingresa un entero o 'q' para terminar.")
        else:
            lista_numeros.append(numero)

def contar_numeros_por_signo(lista_numeros: list[int]) -> tuple[int, int, int]:
    """Cuenta los números positivos, negativos e iguales a cero.

    Returns:
        Tupla con las cantidades de positivos, negativos y ceros,
        en ese orden.
    """
    positivos = 0
    negativos = 0
    ceros = 0

    for numero in lista_numeros:
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            ceros += 1

    return positivos, negativos, ceros

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