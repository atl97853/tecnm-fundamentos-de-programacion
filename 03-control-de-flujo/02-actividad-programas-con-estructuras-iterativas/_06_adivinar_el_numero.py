"""
Programa: Adivinar el número
Autor: Atl
Fecha: Octubre, 2026
Descripción: Genera un número aleatorio entre 1 y 100 y solicita al
usuario que lo adivine. Indica si cada intento es demasiado alto o bajo
y repite el proceso hasta que el usuario acierte.
"""

import random

NUMERO_MINIMO = 1
NUMERO_MAXIMO = 100

def solicitar_intento() -> int:
    """Solicita un intento y repite la petición hasta obtener uno válido."""
    while True:
        try: 
            return int(
                input(
                    f"Ingresa tu intento (un entero del {NUMERO_MINIMO} "
                    f"al {NUMERO_MAXIMO}): "
                )
            )
        except ValueError:
            print("Entrada no válida. Ingresa un número entero.")

def evaluar_intento(intento: int, numero_secreto: int) -> str:
    """Devuelve un mensaje indicando si el intento es demasiado bajo, demasiado alto o correcto."""
    if intento < numero_secreto:
        return "Tu intento es demasiado bajo."
    elif intento > numero_secreto:
        return "Tu intento es demasiado alto."
    else:
        return "¡Acertaste!"

def main() -> None:
    """Ejecuta el juego y ofrece pistas hasta que el usuario acierte."""
    # Se genera una sola vez para mantener el mismo número durante el juego.
    numero_secreto = random.randint(NUMERO_MINIMO, NUMERO_MAXIMO)

    while True:
        # Entrada
        intento = solicitar_intento()

        # Proceso
        mensaje = evaluar_intento(intento, numero_secreto)

        # Salida
        print(mensaje)

        if intento == numero_secreto:
            break

if __name__ == "__main__":
    main()