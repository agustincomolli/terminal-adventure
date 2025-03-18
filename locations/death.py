"""
Este módulo contiene la función `show_death_location` que se encarga de
mostrar un mensaje de muerte y finalizar el juego en la aventura de terminal.
Funciones:
- show_death_location(state: dict) -> dict: Muestra un mensaje de muerte y
    actualiza el estado del juego para reflejar que el jugador ya no está jugando.
Imports:
- print_slowly: Función para imprimir texto lentamente.
- center_text: Función para centrar texto.
- RIP: Arte ASCII que representa una lápida.
"""
from utils import print_slowly, center_text
from assets.art import RIP

def show_death_location(state: dict) -> dict:
    """
    Muestra un mensaje de muerte y finaliza el juego.

    Esta función imprime un mensaje indicando que el jugador ha muerto y
    que la aventura ha terminado. Actualiza el estado del juego para
    reflejar que el jugador ya no está jugando.

    Args:
        state (dict): El estado actual del juego, incluyendo el nombre
                      del jugador y si el juego está en curso.

    Returns:
        dict: El estado actualizado del juego con 'is_playing' establecido
              en False.
    """
    print(center_text(RIP))
    print_slowly("La oscuridad te envuelve...")
    print_slowly("Lamentablemente, tu aventura termina aquí, " +
                 f"{state['player_name']}.")
    print_slowly("Quizás otro aventurero tenga más suerte en el futuro.\n")
    print(center_text("--- FIN DE LA AVENTURA ---"))
    print_slowly(
        "\n¡Has fracasado en Terminal Adventure: La Cueva Misteriosa!")
    state["is_playing"] = False
    return state
