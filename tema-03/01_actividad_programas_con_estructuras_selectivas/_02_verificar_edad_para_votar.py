"""
Programa: Verificar edad para votar
Autor: Atl
Fecha: Octubre, 2026
Descripción: Solicita la edad del usuario y determina si cumple con 
la edad mínima requerida para votar.
"""

# Constantes
EDAD_MINIMA_PARA_VOTAR = 18

def pedir_edad() -> int:
    """Solicita y devuleve una edad entera entre 0 y 120."""
    while True:
        try: 
            edad = int(
                input("Ingresa tu edad: ")
            )
        except ValueError:
            print("Por favor, ingresa una edad real.")
            continue

        if 0 <= edad <= 120:
            return edad
        else:
            print("La edad debe estar entre 0 y 120 años.")

def evaluar_edad_para_votar(edad_usuario: int) -> str:
    """Indica si el usuario cumple la edad mínima para votar."""
    if edad_usuario >= EDAD_MINIMA_PARA_VOTAR:
        return f"Tu edad: {edad_usuario}. Cumples la edad mínima para votar."
    else:
        return f"Tu edad: {edad_usuario}. Aún no cumples la edad mínima para votar."
        
# Bloque principal
if __name__ == "__main__":
    # Entrada
    edad_usuario = pedir_edad()

    # Proceso
    cumple_edad_minima = evaluar_edad_para_votar(edad_usuario)

    # Salida
    print(cumple_edad_minima)