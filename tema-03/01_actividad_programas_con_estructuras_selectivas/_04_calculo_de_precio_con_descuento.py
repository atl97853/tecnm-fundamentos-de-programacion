"""
Programa: Cálculo de precio con descuento
Autor: Atl
Fecha: Octubre, 2026
Descripción: Determina el descuento según el precio original del producto
y calcula su precio final.
"""

def solicitar_precio_producto() -> int:
    """Solicita y devuelve el precio original como un entero no negativo."""
    while True: 
        try:
            precio = int(
                input("Ingresa el precio original del producto (sin decimales): ")
            )
        except ValueError:
            print("Por favor, ingresa un número entero.")
            continue

        if precio >= 0:
            return precio
        else: 
            print("El precio debe ser mayor o igual a 0.")

def calcular_descuento_producto(producto_precio: int) -> int:
    """Calcula el descuento del producto según el precio original"""
    if producto_precio <= 100:
        return 0
    elif producto_precio <= 200:
        return 10
    elif producto_precio <= 500:
        return 20
    else:
        return 25

def calcular_precio_final(producto_precio: int, descuento: int) -> int:
    """Calcula el precio final tras aplicar un descuento porcentual."""
    monto_descuento = producto_precio * (descuento / 100)
    return int(producto_precio - monto_descuento)

# Bloque principal
if __name__ == "__main__":
    # Entrada
    producto_precio = solicitar_precio_producto()

    # Proceso
    descuento = calcular_descuento_producto(producto_precio)
    precio_final = calcular_precio_final(producto_precio, descuento)

    # Salida
    print(
        f"Descuento aplicado: {descuento}%\n"
        f"Total a pagar: ${precio_final}"
    )