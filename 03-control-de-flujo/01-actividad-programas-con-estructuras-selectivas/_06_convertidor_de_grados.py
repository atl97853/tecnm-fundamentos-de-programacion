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
    """Solicita y valida la escala de destino para la conversión."""
    while True: 
        escala_destino = input("¿A qué escala deseas convertir?, escribe 'f' para Fahrenheit o 'k' para Kelvin: ").lower()

        match escala_destino:
            case "f":
                return "fahrenheit"
            case "k":
                return "kelvin"
            case _:
                print("Opción no válida, intentalo de nuevo.")
                continue

def convertir_temperatura(temperatura_celsius: float, escala_destino: str) -> float:
    """Convierte una temperatura de Celsius a Fahrenheit o kelvin."""
    match escala_destino:
        case "fahrenheit":
            return temperatura_celsius * (9 / 5) + 32
        case "kelvin":
            return temperatura_celsius + 273.15

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
    print(
        f"Tu temperatura de {temperatura_celsius} °C equivale a "
        f"{temperatura_convertida} en la escala {escala_destino.capitalize()}."
    )

# Bloque principal
if __name__ == "__main__":
    main()