"""
Este módulo define la función `show_start_location` que muestra la ubicación inicial 
del juego y presenta opciones al jugador.
Funciones:
    - show_start_location(state: dict) -> dict: Muestra la ubicación inicial del 
    juego y presenta opciones al jugador. Dependiendo de la elección del jugador, 
    actualiza el estado del juego con la nueva ubicación o termina el juego.
Importaciones:
    - print_slowly, center_text, get_choice desde utils: Utilidades para imprimir 
      texto lentamente, centrar texto y obtener la elección del jugador.
    - show_inventory desde inventory: Función para mostrar el inventario del jugador.
    - CAVE_ENTRANCE desde assets.art: Arte ASCII de la entrada de la cueva.
"""
from utils import print_slowly, center_text, get_choice
from inventory import show_inventory
from assets.art import CAVE_ENTRANCE


def show_start_location(state: dict) -> dict:
    """
    Muestra la ubicación inicial del juego y presenta opciones al jugador.
    La función imprime una descripción de la ubicación inicial utilizando la función `print_slowly`.
    Luego, presenta al jugador tres opciones:
    1. Entrar a la cueva
    2. Explorar los alrededores
    3. Revisar tu inventario
    Dependiendo de la elección del jugador, la función retorna una cadena que indica la siguiente 
    ubicación:
    - "cave" si el jugador elige entrar a la cueva.
    - "forest" si el jugador elige explorar los alrededores.
    - "start" si el jugador elige revisar su inventario (después de mostrar el inventario).

    Returns:
        str: La siguiente ubicación basada en la elección del jugador.
    """
    print(center_text(CAVE_ENTRANCE))
    print_slowly("Te encuentras frente a la entrada de una misteriosa cueva.")
    print_slowly("Los lugareños hablan de un tesoro oculto en su interior, " +
                 "pero nadie ha regresado para contarlo.")
    print_slowly("El viento sopla suavemente, como si la cueva respirara...\n")

    options: list[str] = ["Entrar a la cueva",
                          "Explorar los alrededores",
                          "Revisar tu inventario",
                          "Salir del juego"]
    choice = get_choice(options)

    if choice == 1:
        state["location"] = "cave"
    elif choice == 2:
        state["location"] = "forest"
    elif choice == 3:
        show_inventory(state)
    else:
        state["is_playing"] = False

    return state
