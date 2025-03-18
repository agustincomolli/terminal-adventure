"""
Este módulo define la función `show_forest_location` que permite al jugador 
interactuar con la ubicación del bosque en el juego de aventura por terminal.
Funciones:
- show_forest_location(state: dict) -> dict: Muestra la ubicación del bosque y
  permite al jugador interactuar con el entorno, actualizando el estado del juego 
  según las decisiones del jugador.
Importa las siguientes funciones y constantes de otros módulos:
- `print_slowly`, `center_text`, `get_choice` de `..utils`
- `POTION`, `FOREST` de `..assets.art`
- `show_inventory` de `..inventory`
"""
from utils import print_slowly, center_text, get_choice
from assets.art import POTION, FOREST
from inventory import show_inventory

def show_forest_location(state: dict) -> dict:
    """
    Muestra la ubicación del bosque y permite al jugador interactuar con el entorno.
    Args:
        state (dict): El estado actual del juego, que incluye información sobre el inventario 
                      y la ubicación del jugador.
    Returns:
        dict: El estado actualizado del juego después de la interacción del jugador en el bosque.
    """
    print(center_text(FOREST))
    print_slowly("Te adentras en el bosque que rodea la cueva.")
    print_slowly("Los árboles son altos y el follaje es denso.")

    if not state["has_potion"]:
        print_slowly("Encuentras un arbusto con bayas rojas brillantes.\n")

        options = ["Recoger las bayas", "Ignorar las bayas",
                   "Revisar tu inventario", "Volver a la entrada de la cueva"]
        choice = get_choice(options)

        if choice == 1:
            print_slowly("Recoges las bayas y las mezclas con agua de " +
                         "un arroyo cercano.\n")
            print(center_text(POTION))
            print(center_text("¡Has creado una Poción curativa!"))
            state["has_potion"] = True
        elif choice == 2:
            print_slowly("Decides no tocar las bayas desconocidas.")
        elif choice == 3:
            show_inventory(state)
        else:
            state["location"] = "start"
    else:
        print_slowly("El bosque parece tranquilo, pero sientes que hay algo " +
                     "importante en la cueva.\n")

        options = ["Explorar más el bosque",
                   "Revisar tu inventario",
                   "Volver a la entrada de la cueva"]
        choice = get_choice(options)

        if choice == 1:
            print_slowly("Exploras más profundamente el bosque...")
            print_slowly("Después de un rato, te das cuenta de que estás " +
                         "dando vueltas en círculos.")
            print("Decides regresar al punto de partida.")
        elif choice == 2:
            show_inventory(state)
        else:
            state["location"] = "start"

    input("\nPresione ENTER para continuar...")
    return state
