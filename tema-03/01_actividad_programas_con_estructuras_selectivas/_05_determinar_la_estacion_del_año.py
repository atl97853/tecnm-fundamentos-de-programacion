"""
Programa: Determinar la estación del año
Autor: Atl
Fecha: Octubre, 26
Descripción: Solicita al usuario un número de mes y muestra
la estación del año correspondiente. 
"""

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