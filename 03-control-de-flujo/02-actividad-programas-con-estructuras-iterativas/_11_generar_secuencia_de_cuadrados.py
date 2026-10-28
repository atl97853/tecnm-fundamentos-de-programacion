"""
Programa: Generar secuencia de cuadrados (con do-while simulado)
Autor: Atl
Fecha: Octubre, 2026
Descripción: Solicita un número entero positivo y muestra los cuadrados
de los números desde 1 hasta ese límite mediante un bucle do-while simulado.
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

def calcular_cuadrado(numero: int) -> int:
    """Devuelve el cuadrado del número recibido."""
    return numero ** 2

def mostrar_cuadrados_hasta(limite: int) -> None:
    """Muestra los cuadrados de los enteros desde 1 hasta el límite."""
    numero_actual = 1

    while True:
        print(calcular_cuadrado(numero_actual))
        numero_actual += 1

        if numero_actual > limite:
            break

def main() -> None:
    """Solicita un límite positivo y muestra los cuadrados hasta él."""
    # Entrada
    limite = solicitar_entero_positivo()

    # Proceso y salida
    mostrar_cuadrados_hasta(limite)

if __name__ == "__main__":
    main()