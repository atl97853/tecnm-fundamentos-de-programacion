"""
Programa: Verificar edad para votar
Autor: Atl
Fecha: Octubre de 2026
Descripción: Solicita la edad del usuario y determina si cumple con 
la edad mínima requerida para votar.
"""

# Constantes
EDAD_MINIMA_PARA_VOTAR = 18

# Bloque principal
if __name__ == "__main__":
    # Entrada
    edad_usuario = pedir_edad()

    # Proceso
    cumple_edad_minima = evaluar_edad_para_votar(edad_usuario)

    # Salida
    print(cumple_edad_minima)