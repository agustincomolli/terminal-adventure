"""
Este módulo contiene la función principal para el juego "Terminal Adventure: La Cueva Misteriosa".
Funciones:
- main: Función principal que inicializa el estado del juego y controla el flujo del mismo.
El juego comienza mostrando el título y el logo, y luego solicita al jugador que ingrese su nombre.
Dependiendo de la ubicación actual del jugador, se llama a la función correspondiente para mostrar
la ubicación y manejar las interacciones del jugador.
Importa los siguientes módulos:
- time: Para manejar retrasos en la ejecución.
- .assets.art: Para mostrar el título y el logo del juego.
- .utils: Para funciones auxiliares como limpiar la pantalla, imprimir texto lentamente y 
  centrar texto.
- .locations: Para manejar las diferentes ubicaciones del juego, como el inicio, la cueva, 
  la izquierda, la derecha, el tesoro, el dragón, el bosque, la victoria y la muerte.
"""
import time
from assets.art import TITLE, CAVE_LOGO
from utils import clear, print_slowly, center_text
from locations import start, cave, left, right, treasure, dragon, forest, victory, death


def main() -> None:
    """ Función principal del programa """
    state = {
        "location": "start",
        "health": 100,
        "is_playing": True,
        "has_key": False,
        "has_potion": False,
        "has_sword": False,
        "player_name": ""
    }

    # Limpiar la pantalla.
    clear()

    print(center_text(TITLE), end="")
    print(center_text(CAVE_LOGO))
    time.sleep(2)

    print_slowly("¡Bienvenido a Terminal Adventure: La Cueva Misteriosa!")
    while not state["player_name"]:
        state["player_name"] = input("\n¿Cuál es tu nombre, " +
                                     "aventurero? > ").strip()
        if not state["player_name"]:
            print("El nombre no puede estar vacío. Intenta de nuevo.")
    print(f"\n¡Saludos, {state["player_name"]}!\n")

    # Esperar un segundo.
    time.sleep(1)

    while state["is_playing"]:
        clear()
        if state["location"] == "start":
            start.show_start_location(state)
        elif state["location"] == "cave":
            cave.show_cave_location(state)
        elif state["location"] == "left":
            left.show_left_location(state)
        elif state["location"] == "right":
            right.show_right_location(state)
        elif state["location"] == "treasure":
            treasure.show_treasure_location(state)
        elif state["location"] == "dragon":
            dragon.show_dragon_location(state)
        elif state["location"] == "forest":
            forest.show_forest_location(state)
        elif state["location"] == "exit":
            victory.show_victory_location(state)
        elif state["location"] == "death":
            death.show_death_location(state)


if __name__ == "__main__":
    main()
