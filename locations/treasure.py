"""
Este módulo contiene la función `show_treasure_location` que maneja la lógica
cuando el jugador encuentra la ubicación del tesoro en el juego de aventura
terminal. Permite al jugador tomar decisiones sobre cómo interactuar con el
tesoro encontrado.
Funciones:
    show_treasure_location(state: dict) -> dict:
        Actualiza y devuelve el estado del juego basado en la elección del jugador.
"""
import time
from utils import print_slowly, center_text, get_choice
from assets.art import TREASURE
from inventory import show_inventory

def show_treasure_location(state: dict) -> dict:
    """
    Muestra la ubicación del tesoro y permite al jugador tomar una decisión.
    Args:
        state (dict): El estado actual del juego.
    Returns:
        dict: El estado actualizado del juego después de la elección del jugador.    
    """
    print(center_text(TREASURE))
    print_slowly("¡Entras en una cámara llena de tesoros brillantes!")
    print_slowly("Oro, joyas y artefactos antiguos llenan la sala.")
    print_slowly("En el centro hay un cofre particularmente grande.\n")

    options = ["Abrir el cofre central", "Recoger algunas monedas",
               "Revisar tu inventario", "Salir de la cámara"]
    choice = get_choice(options)

    if choice == 1:
        print_slowly("Te acercas al cofre central con cautela...")
        print_slowly("Al abrirlo...")
        time.sleep(1.5)
        print_slowly("¡UN DRAGÓN DESPIERTA DETRÁS DE TI!")
        state["location"] = "dragon"
    elif choice == 2:
        print_slowly("Recoges algunas monedas de oro y las guardas.")
        print_slowly("Sientes tus bolsillos muy pesados...")
    elif choice == 3:
        show_inventory(state)
    else:
        state["location"] = "right"

    input("\nPresione ENTER para continuar...")
    return state
