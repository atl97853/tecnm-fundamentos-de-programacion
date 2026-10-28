"""
Programa: Contador de números impares (con do-while simulado)
Autor: Atl
Fecha: Octubre, 2026
Descripción: Solicita un número entero positivo y muestra todos los números
impares desde 1 hasta ese límite mediante un bucle do-while simulado.
"""

def solicitar_entero_positivo() -> int:
    """Solicita un entero positivo hasta que el usuario ingrese uno válido."""
    while True:
        try:
            numero = int(input("Ingresa un número entero positivo: "))
        except ValueError:
            print("Ingresa un número entero válido.")
            continue

        if numero > 0:
            return numero
        else: 
            print("El número debe ser mayor que cero.")

def mostrar_impares_hasta(limite: int) -> None:
    """Muestra los números impares desde 1 hasta el límite, inclusive."""
    impar_actual = 1

    while True:
        print(impar_actual)
        # Los enteros consecutivos tienen paridad opuesta: sumar 1 a un impar
        # produce un par, y sumar otro 1 produce el siguiente impar. Por eso,
        # sumar 2 conserva la paridad: n + 2 ≡ n (mod 2).
        impar_actual += 2

        if impar_actual > limite:
            break

def main() -> None:
    """Solicita un límite y muestra los números impares hasta él."""
    # Entrada
    limite = solicitar_entero_positivo()

    # Proceso y salida
    mostrar_impares_hasta(limite)

if __name__ == "__main__":
    main()
    