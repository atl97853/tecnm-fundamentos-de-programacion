"""
Programa: Conversor de monedas
Autor: Atl
Fecha: Octubre, 2026
Descripción: Convierte un monto en pesos mexicanos a la moneda
seleccionada por el usuario.
"""

def main() -> None:
    """Solicita un monto en pesos mexicanos y muestra su conversión.

    El usuario selecciona la moneda de destino.
    """
    # Entrada
    monto_pesos = pedir_monto_pesos()
    moneda_destino = seleccionar_moneda_destino()

    # Proceso
    monto_convertido = convertir_pesos(monto_pesos, moneda_destino)

    # Salida
    print(monto_convertido)

# Bloque principal
if __name__ == "__main__":
    main()