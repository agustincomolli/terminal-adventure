"""
Este módulo contiene la función `show_victory_location` que muestra el mensaje
de victoria y finaliza el juego en el proyecto Terminal Adventure.
Funciones:
- show_victory_location(state: dict) -> dict: Muestra el mensaje de victoria,
    actualiza el estado del juego y finaliza la partida.
Imports:
- print_slowly: Función para imprimir texto lentamente.
- center_text: Función para centrar texto.
- VICTORY: Arte ASCII que representa la victoria.
"""
from utils import print_slowly, center_text
from assets.art import VICTORY

def show_victory_location(state: dict) -> dict:
    """
    Muestra el mensaje de victoria y finaliza el juego.

    Esta función imprime un mensaje de victoria, felicitando al jugador por
    haber conseguido el tesoro y derrotado al dragón. Luego, actualiza el
    estado del juego para indicar que el jugador ha terminado de jugar.

    Args:
        state (dict): El estado actual del juego, incluyendo el nombre del
                      jugador y si el juego está en curso.

    Returns:
        dict: El estado actualizado del juego, con 'is_playing' establecido
              en False.
    """
    print(center_text(VICTORY))
    print_slowly("¡Has conseguido el tesoro y derrotado al dragón!")
    print_slowly(f"Felicidades, {state['player_name']}! Tu valentía " +
                 "será recordada en las leyendas.")
    print_slowly("El tesoro del dragón contiene riquezas más allá " +
                 "de tus sueños.\n")
    print(center_text("--- FIN DE LA AVENTURA ---"))
    print_slowly("\n¡Has completado Terminal Adventure: La Cueva Misteriosa!")
    state["is_playing"] = False
    return state
