"""
Programa: Convertidor de grados
Autor: Atl
Fecha: Octubre, 2026
Descripción: Convierte una temperatura en grados Celsius a grados
Fahrenheit o kelvin, según la escala elegida por el usuario.
"""

def pedir_temperatura_celsius() -> float:
    """Solicita y valida una temperatura en grados Celsius.

    Repite la solicitud hasta obtener un número mayor o igual a -273.15 °C.

    Returns:
        float: Temperatura validada en grados Celsius.
    """
    while True:
        try:
            temperatura_celsius = float(
                input("Ingresa la temperatura en grados Celsius (°C): ")
            )
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if temperatura_celsius >= -273.15:
            return temperatura_celsius
        else: 
            print(
                "La temperatura debe ser mayor o igual a "
                "-273.15 °C (cero absoluto)."
            )

def seleccionar_escala_destino() -> str:
    """Solicita y valida la escala de destino para la conversión.

    Repite la solicitud hasta recibir 'f' o 'k'.

    Returns:
        str: "fahrenheit" o "kelvin", según la opción seleccionada.
    """
    while True: 
        escala_destino = input("¿A qué escala deseas convertir? Escribe 'f' para Fahrenheit o 'k' para Kelvin: ").lower()

        match escala_destino:
            case "f":
                return "fahrenheit"
            case "k":
                return "kelvin"
            case _:
                print("Opción no válida, intentalo de nuevo.")
                continue

def main() -> None:
    """Solicita la temperatura en Celsius y muestra su conversión.
    El usuario elige Fahrenheit o kelvin como escala de destino.
    """
    # Entrada
    temperatura_celsius = pedir_temperatura_celsius()
    escala_destino = seleccionar_escala_destino()

    # Proceso
    temperatura_convertida = convertir_temperatura(
        temperatura_celsius, escala_destino
    )

    # Salida
    print(f"{temperatura_convertida}")

# Bloque principal
if __name__ == "__main__":
    main()