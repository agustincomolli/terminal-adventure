"""
Este módulo contiene la función `show_right_location`, que maneja las interacciones del jugador
cuando se encuentra en la ubicación a la derecha en la aventura. La función actualiza el estado
del juego basado en las decisiones del jugador, como tomar una poción, revisar el inventario,
o usar una llave para abrir una puerta.
Funciones:
    show_right_location(state: dict) -> dict:
"""
from utils import print_slowly, center_text, get_choice
from assets.art import POTION, RIGHT
from inventory import show_inventory

def show_right_location(state: dict) -> dict:
    """
    Muestra la ubicación a la derecha en la aventura y maneja las interacciones del jugador.
    Args:
        state (dict): El estado actual del juego, que incluye información sobre el 
                      inventario del jugador y su ubicación.
    Returns:
        dict: El estado actualizado del juego después de las interacciones del jugador 
              en esta ubicación.
    """
    print(center_text(RIGHT))
    print_slowly(
        "Sigues el camino de la derecha, que se estrecha cada vez más.")
    print_slowly(
        "Escuchas un goteo constante y percibes un brillo al final del túnel.")

    if not state["has_potion"]:
        print_slowly(
            "Encuentras un estante con una poción de color rojo brillante.\n")

        options = ["Tomar la poción", "Dejarla e investigar más adelante",
                   "Revisar tu inventario", "Volver atrás"]
        choice = get_choice(options)

        if choice == 1:
            state["has_potion"] = True
            print(center_text(POTION))
            print(center_text("¡Has obtenido una Poción curativa!"))
        elif choice == 2:
            print_slowly("Decides dejar la poción por ahora.")
        elif choice == 3:
            show_inventory(state)
        else:
            state["location"] = "cave"
    else:
        print_slowly("El brillo que veías al final del túnel proviene de " +
                     "una puerta dorada.")
        print_slowly("La puerta tiene una cerradura resplandeciente.")
        if not state["has_key"]:
            print_slowly("Necesitas una llave para abrir esta puerta.\n")

            options = ["Revisar tu inventario", "Volver atrás"]
            choice = get_choice(options)

            if choice == 1:
                show_inventory(state)
            else:
                state["location"] = "cave"
        else:
            print()
            options = ["Usar la llave dorada",
                       "Revisar tu inventario", "Volver atrás"]
            choice = get_choice(options)

            if choice == 1:
                print_slowly("¡La llave encaja perfectamente!")
                print_slowly("La puerta se abre lentamente...")
                state["location"] = "treasure"
            elif choice == 2:
                show_inventory(state)
            else:
                state["location"] = "cave"

    input("\nPresione ENTER para continuar...")
    return state
