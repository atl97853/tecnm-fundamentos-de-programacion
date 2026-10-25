"""
Programa: Brindar información
Autor: Atl
Fecha: Octubre, 2026
Descripción: Muestra información sobre cinco novelas ligeras japonesas
a partir del título ingresado por el usuario.
"""

# Constantes
MENU_NOVELAS = """Novelas disponibles:
- Mushoku Tensei
- Secrets of the Silent Witch
- Ascendance of a Bookworm
- Violet Evergarden
- The Saga of Tanya the Evil
"""

INFORMACION_MUSHOKU_TENSEI = """Título: Mushoku Tensei
País de origen: Japón
Autor: Rifujin na Magonote
Descripción: Un hombre reencarna como Rudeus Greyrat en un mundo de magia
y decide aprovechar su segunda oportunidad para empezar de nuevo.
Última publicación: 2022-11-25
Adaptación al anime: Sí.
Protagonista: Rudeus Greyrat
Próximo lanzamiento: Desconocido.
"""

INFORMACION_SILENT_WITCH = """Título: Secrets of the Silent Witch
País de origen: Japón
Autor: Matsuri Isora
Descripción: Una maga prodigio extremadamente tímida debe proteger en secreto
a un príncipe mientras estudia en una academia.
Última publicación: 2026-06-10
Adaptación al anime: Sí.
Protagonista: Monica Everett
Próximo lanzamiento: 2026-11-10
"""

INFORMACION_BOOKWORM = """Título: Ascendance of a Bookworm
País de origen: Japón
Autor: Miya Kazuki
Descripción: Una amante de los libros reencarna como Myne en un mundo donde
los libros son escasos y decide fabricarlos para poder leer.
Última publicación: 2023-12-09
Adaptación al anime: Sí.
Protagonista: Myne / Rozemyne
Próximo lanzamiento: Desconocido.
"""

INFORMACION_VIOLET_EVERGARDEN = """Título: Violet Evergarden
País de origen: Japón
Autor: Kana Akatsuki
Descripción: Una antigua soldado trabaja escribiendo cartas para otras personas
mientras aprende a comprender sus emociones y el significado del amor.
Última publicación: 2020-03-27
Adaptación al anime: Sí.
Protagonista: Violet Evergarden
Próximo lanzamiento: Novela finalizada.
"""

INFORMACION_TANYA = """Título: The Saga of Tanya the Evil
País de origen: Japón
Autor: Carlo Zen
Descripción: Un oficinista reencarna como Tanya en un mundo en guerra, donde
utiliza sus conocimientos para ascender en un ejército que combina
magia y tecnología.
Última publicación: 2023-09-29
Adaptación al anime: Sí.
Protagonista: Tanya Degurechaff
Próximo lanzamiento: Desconocido.
"""

def main() -> None:
    """Solicita un título válido y muestra la información de la novela."""
    print(MENU_NOVELAS)

# Bloque principal
if __name__ == "__main__":
    main()