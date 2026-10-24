"""
Programa: Conversor de monedas
Autor: Atl
Fecha: Octubre, 2026
Descripción: Convierte un monto en pesos mexicanos a la moneda
seleccionada por el usuario.
"""

# Constantes. 
# Tasas de referencia: unidades de cada moneda por 1 MXN.
USD = 0.053490
EUR = 0.047705
THB = 1.803355
JPY = 8.403207
KRW = 70.946254
AUD = 0.076202
PEN = 0.184191
CAD = 0.074999
VES = 47.145678
ARS = 81.680564

MENU_MONEDAS = """[1] Dólar (USD)
[2] Euro (EUR)
[3] Bath (THB)
[4] Yen (JPY)
[5] Won (KRW)
[6] Dólar Australiano (AUD)
[7] Sol (PEN)
[8] Dólar Canadiense (CAD)
[9] Bolívar (VES)
[10] Peso Argentino (ARS)"""

# Cálculo y formato del resultado
def generar_mensaje_conversion(monto_pesos: float, tipo_cambio: float, codigo_moneda: str) -> str:
    """Convierte un monto en MXN y devuelve el resultado como mensaje."""
    monto_convertido = monto_pesos * tipo_cambio

    return (
        f"Tu monto de {monto_pesos:.2f} MXN equivale a "
        f"{monto_convertido:.2f} {codigo_moneda}."
    )

# Entrada de datos y selección de moneda
def pedir_monto_pesos() -> float:
    """Solicita un monto numérico en pesos mexicanos mayor o igual a cero."""
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

def seleccionar_y_convertir_moneda(monto_pesos: float) -> str:
    """Solicita una moneda válida y devuelve el mensaje de conversión."""
    print(MENU_MONEDAS)

    while True:
        opcion_moneda = input(
            "¿A qué moneda deseas convertir? "
            "Ingresa una opción del 1 al 10: "
        ).strip()

        match opcion_moneda:
            case "1":
                return generar_mensaje_conversion(monto_pesos, USD, "USD")
            case "2":
                return generar_mensaje_conversion(monto_pesos, EUR, "EUR")
            case "3":
                return generar_mensaje_conversion(monto_pesos, THB, "THB")
            case "4":
                return generar_mensaje_conversion(monto_pesos, JPY, "JPY")
            case "5":
                return generar_mensaje_conversion(monto_pesos, KRW, "KRW")
            case "6":
                return generar_mensaje_conversion(monto_pesos, AUD, "AUD")
            case "7":
                return generar_mensaje_conversion(monto_pesos, PEN, "PEN")
            case "8":
                return generar_mensaje_conversion(monto_pesos, CAD, "CAD")
            case "9":
                return generar_mensaje_conversion(monto_pesos, VES, "VES")
            case "10":
                return generar_mensaje_conversion(monto_pesos, ARS, "ARS")
            case _:
                print(
                    "Opción no válida."
                    "Elige una de las opciones del menú."
                )

# Programa principal
def main() -> None:
    """Solicita el monto y la moneda de destino y muestra la conversión."""
    # Entrada
    monto_pesos = pedir_monto_pesos()

    # Proceso
    mensaje_conversion = seleccionar_y_convertir_moneda(monto_pesos)

    # Salida
    print(mensaje_conversion)

# Bloque principal
if __name__ == "__main__":
    main()