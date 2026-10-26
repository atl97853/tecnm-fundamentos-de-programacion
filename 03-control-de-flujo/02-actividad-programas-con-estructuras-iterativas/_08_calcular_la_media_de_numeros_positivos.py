"""
Programa: Media de números positivos
Autor: Atl
Fecha: Octubre, 2026
Descripción: Solicita números hasta ingresar uno negativo y muestra
la media de los positivos. El cero no se incluye en el cálculo.
"""

import math

def solicitar_numero() -> float:
    """Solicita un número finito y repite la petición hasta obtenerlo. Acepta enteros y decimales."""
    while True:
        entrada = input(
            "Ingresa un número positivo (o uno negativo para terminar): "
        )

        try:
            numero = float(entrada)
        except ValueError:
            print("Entrada no válida. Ingresa un número válido.")
            continue

        if math.isfinite(numero):
            return numero

        print("Entrada no válida. Ingresa un número finito.")


def calcular_media(suma: float, cantidad: int) -> float | None:
    """Calcula la media a partir de una suma y su cantidad de valores.

    Args:
        suma: Suma de los números positivos ingresados.
        cantidad: Cantidad de números positivos; debe ser no negativa.

    Returns:
        Media de los valores, o None si la cantidad es cero.
    """
    if cantidad == 0:
        return None

    return suma / cantidad


def main() -> None:
    """Solicita números y muestra la media de los positivos al terminar."""
    suma_positivos = 0.0
    cantidad_positivos = 0

    while True:
        # Entrada
        numero = solicitar_numero()

        if numero < 0:
            break

        # Proceso
        if numero > 0:
            suma_positivos += numero
            cantidad_positivos += 1
        else:
            print("El cero no se incluye en la media.")

    media = calcular_media(suma_positivos, cantidad_positivos)

    # Salida
    if media is None:
        print("No se ingresaron números positivos; no se puede calcular la media.")
    else:
        print(f"Media de los números positivos: {media}.")

if __name__ == "__main__":
    main()