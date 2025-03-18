"""
Este módulo define la función `show_cave_location` que muestra la ubicación de la 
cueva en un juego de aventuras basado en texto. Permite al jugador elegir una acción 
y actualiza el estado del juego en consecuencia.
Funciones:
- show_cave_location(state: dict) -> dict: Muestra la ubicación de la cueva y permite 
  al jugador elegir una acción. Actualiza y devuelve el estado del juego.
Importaciones:
- print_slowly: Función para imprimir texto lentamente.
- center_text: Función para centrar texto.
- get_choice: Función para obtener la elección del jugador.
- CAVE: Arte ASCII de la cueva.
- show_inventory: Función para mostrar el inventario del jugador.
"""
from utils import print_slowly, center_text, get_choice
from assets.art import CAVE
from inventory import show_inventory


def show_cave_location(state: dict) -> dict:
    """
    Muestra la ubicación de la cueva y permite al jugador elegir una acción.
    Args:
        state (dict): El estado actual del juego, que incluye la ubicación y otros datos relevantes.
    Returns:
        dict: El estado actualizado del juego después de la elección del jugador.
    """
    print(center_text(CAVE))
    print_slowly("Entras a la cueva. Está oscuro y húmedo.")
    print_slowly("Tus pasos resuenan en las paredes rocosas.")
    print_slowly("A medida que tus ojos se adaptan a la oscuridad, " +
                 "notas que el camino se bifurca.\n")

    options = ["Ir hacia la izquierda", "Ir hacia la derecha",
               "Revisar tu inventario", "Volver a la entrada"]

    choice = get_choice(options)

    if choice == 1:
        state["location"] = "left"
    elif choice == 2:
        state["location"] = "right"
    elif choice == 3:
        show_inventory(state)
    else:
        state["location"] = "start"
    return state
