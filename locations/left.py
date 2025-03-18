"""
Este módulo define la función `show_left_location` que maneja la lógica del juego 
cuando el jugador se mueve a la ubicación a la izquierda en la cueva. Permite al 
jugador tomar decisiones como tomar una espada, una llave, revisar el inventario 
o volver atrás.
Funciones:
    - show_left_location(state: dict) -> dict: Muestra la ubicación a la izquierda 
      en la cueva y permite al jugador tomar decisiones, actualizando el estado del 
      juego en consecuencia.
Importa:
    - print_slowly, center_text, get_choice desde utils.
    - LEFT, LEFT_SWORD, SWORD, KEY desde assets.art.
    - show_inventory desde inventory.
"""
from utils import print_slowly, center_text, get_choice
from assets.art import LEFT, LEFT_SWORD, SWORD, KEY
from inventory import show_inventory


def show_left_location(state: dict) -> dict:
    """
    Muestra la ubicación a la izquierda en la cueva y permite al jugador tomar decisiones.
    Args:
        state (dict): El estado actual del juego, que incluye información sobre 
                      si el jugador tiene la espada y la llave, y la ubicación actual.
    Return:
        dict: El estado actualizado del juego después de que el jugador haya tomado una decisión.    
    """
    if not state["has_sword"]:
        print(center_text(LEFT_SWORD))
        print_slowly("Sigues el camino de la izquierda, que desciende " +
                     "profundamente en la cueva.")
        print_slowly(
            "El aire se vuelve más frío y escuchas un sonido metálico.")
        print_slowly("¡Encuentras una espada antigua clavada en una roca!\n")
        options = ["Tomar la espada", "Dejarla e investigar más adelante",
                   "Revisar tu inventario", "Volver atrás"]

        choice = get_choice(options)
        if choice == 1:
            state["has_sword"] = True
            print(center_text(SWORD))
            print(center_text("¡Has obtenido una espada antigua!"))
        elif choice == 2:
            print_slowly("Decides dejar la espada por ahora.")
        elif choice == 3:
            show_inventory(state)
        else:
            state["location"] = "cave"
    else:
        print(center_text(LEFT))
        print_slowly("Sigues el camino de la izquierda, que desciende " +
                     "profundamente en la cueva.")
        print_slowly(
            "El aire se vuelve más frío y escuchas un sonido metálico.")
        print_slowly("Continúas por el camino y llegas a una pequeña cámara.")

        if not state["has_key"]:
            print_slowly(
                "¡En un rincón brillante, encuentras una llave dorada!\n")
            options = ["Tomar la llave", "Dejarla por ahora",
                       "Revisar tu inventario", "Volver atrás"]
            choice = get_choice(options)
            if choice == 1:
                state["has_key"] = True
                print(center_text(KEY))
                print("¡Has obtenido una Llave dorada!")
            elif choice == 2:
                print_slowly("Decides dejar la llave por ahora.")
            elif choice == 3:
                show_inventory(state)
            else:
                state["location"] = "cave"
        else:
            print_slowly(
                "No parece haber nada más interesante en esta cámara.\n")
            options = ["Revisar tu inventario", "Volver atrás"]
            choice = get_choice(options)
            if choice == 1:
                show_inventory(state)
            else:
                state["location"] = "cave"

    input("\nPresione ENTER para continuar...")
    return state
