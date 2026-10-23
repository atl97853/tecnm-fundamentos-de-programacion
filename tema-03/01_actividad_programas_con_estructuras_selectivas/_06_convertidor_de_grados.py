"""
Programa: Convertidor de grados
Autor: Atl
Fecha: Octubre, 26
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

def main() -> None:
    """Solicita la temperatura en Celsius y muestra su conversión.
    El usuario elige Fahrenheit o kelvin como escala de destino.
    """
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