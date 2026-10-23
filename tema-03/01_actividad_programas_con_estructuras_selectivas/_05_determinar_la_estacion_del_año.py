"""
Programa: Determinar la estación del año
Autor: Atl
Fecha: Octubre, 26
Descripción: Solicita al usuario un número de mes y muestra
la estación del año correspondiente. 
"""

def pedir_numero_mes() -> int:
    """Solicita y valida un número de mes entre 1 y 12."""
    while True: 
        try:
            numero_mes = int(
                input("Ingresa el número del mes (1 a 12): ")
            )
        except ValueError:
            print("Por favor, ingresa un número entero.")
            continue

        if  1 <= numero_mes <= 12:
            return numero_mes
        else: 
            print("El número del mes debe estar entre 1 y 12.")

def main() -> None:
    """Solicita un número de mes y muestra la estación correspondiente."""
    # Entrada
    numero_mes = pedir_numero_mes()

    # Proceso
    estacion_año = determinar_estacion(numero_mes)

    # Salida
    print(f"{estacion_año}")

# Bloque principal
if __name__ == "__main__":
    main()