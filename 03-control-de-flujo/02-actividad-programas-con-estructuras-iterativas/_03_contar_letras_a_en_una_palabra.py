"""
Programa: Contar letras 'a' en una palabra
Autor: Atl
Fecha: Octubre, 2026
Descripción: Solicita una palabra, cuenta las apariciones de la letra
minúscula 'a' y muestra el resultado en la terminal.
"""
def solicitar_palabra() -> str:
    """Solicita una palabra al usuario y la devuelve."""
    return ""

def contar_letras_a(palabra: str) -> int:
    """Cuenta las apariciones de la letra minúscula 'a' en una palabra.

    Returns:
        Cantidad de apariciones de la letra 'a'. Devuelve 0 si no aparece.
    """
    return 0

def main() -> None:
    """Solicita una palabra y muestra la cantidad de letras 'a'."""
    # Entrada
    palabra = solicitar_palabra()

    # Proceso
    cantidad_a = contar_letras_a(palabra)

    # Salida
    print(f"Cantidad de letras 'a' en '{palabra}': {cantidad_a}.")


if __name__ == "__main__":
    main()