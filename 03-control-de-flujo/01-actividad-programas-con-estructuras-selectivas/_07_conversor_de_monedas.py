"""
Programa: Conversor de monedas
Autor: Atl
Fecha: Octubre, 2026
Descripción: Convierte un monto en pesos mexicanos a la moneda
seleccionada por el usuario.
"""

# Constantes. 
# Tasas de cambio, 1 peso mexicano equivale a:
USD = 0.053
EUR = 0.047
THB = 1.80
JPY = 8.36
KRW = 71.01
AUD = 0.075
PEN = 0.18
CAD = 0.074
VES = 47.85
ARS = 81.53

def pedir_monto_pesos() -> float:
    """Solicita y valida un monto numérico en pesos mexicanos."""
    while True:
        try:
            monto_pesos = float(
                input("Ingresa el monto en pesos mexicanos (MXN): ")
            )
        except ValueError:
            print("Por favor, ingresa una cantidad válida.")
            continue

        if monto_pesos >= 0:
            return monto_pesos
        else: 
            print("Por favor, ingresa un monto mayor o igual a 0.")

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