"""
Programa: Vocales o consonantes
Autor: Atl
Fecha: Octubre, 2026
Descripción: Clasifica letras mayúsculas y minúsculas como vocales o
consonantes hasta que el usuario ingrese un espacio.
"""

VOCALES = "aeiouáéíóúü"

def solicitar_letra() -> str:
    """Solicita una letra o un espacio y repite las entradas no válidas.

    Returns:
        Una letra, conservando las mayúsculas, o " " para terminar.
    """
    while True:
        entrada = input("Ingresa una letra o un espacio para terminar: ")

        if entrada == " ":
            return entrada

        if len(entrada) == 1 and entrada.isalpha():
            return entrada

        print("Entrada no válida. Ingresa una sola letra o un espacio.")

def clasificar_letra(letra: str) -> str:
    """Devuelve 'vocal' o 'consonante' para una letra validada.

    Considera mayúsculas y minúsculas, incluidas las vocales con tilde y ü.
    """
    if letra.lower() in VOCALES:
        return "vocal"

    return "consonante"

def main() -> None:
    """Solicita y clasifica letras hasta que el usuario ingrese un espacio."""
    while True:
        # Entrada
        letra = solicitar_letra()

        if letra == " ":
            break

        # Proceso
        tipo_letra = clasificar_letra(letra)

        # Salida
        print(f"La letra '{letra}' es una {tipo_letra}.")
        
if __name__ == "__main__":
    main()