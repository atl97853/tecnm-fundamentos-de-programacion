"""
Programa: Cálculo de precio con descuento
Autor: Atl
Fecha: Octubre, 2026
Descripción: Determina el descuento según el precio original del producto
y calcula su precio final.
"""

# Bloque principal
if __name__ == "__main__":
    # Entrada
    producto_precio = solicitar_precio_producto()

    # Proceso
    precio_final = calcular_descuento_producto(producto_precio)

    # Salida
    print(precio_final)