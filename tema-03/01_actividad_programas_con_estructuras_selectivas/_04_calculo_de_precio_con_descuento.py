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

# Bloque principal
if __name__ == "__main__":
    # Entrada
    producto_precio = solicitar_precio_producto()

    # Proceso
    precio_final = calcular_descuento_producto(producto_precio)

    # Salida
    print(precio_final)