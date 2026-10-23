"""
Programa: Convertidor de grados
Autor: Atl
Fecha: Octubre, 26
Descripción: Convierte una temperatura en grados Celsius a grados
Fahrenheit o kelvin, según la escala elegida por el usuario.
"""

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