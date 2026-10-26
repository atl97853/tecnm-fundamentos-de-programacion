"""
Programa: Imprimir números divisibles por 3 y 5
Autor: Atl
Fecha: Octubre, 2026
Descripción: Imprime los números enteros del 1 al 100, ambos incluidos,
que son divisibles tanto por 3 como por 5.
"""

def imprimir_divisibles_por_3_y_5() -> None:
    """Imprime los enteros del 1 al 100 divisibles tanto por 3 como por 5."""
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(numero)

def main() -> None:
    """Ejecuta la impresión de los múltiplos comunes de 3 y 5."""
    imprimir_divisibles_por_3_y_5()

if __name__ == "__main__":
    main()