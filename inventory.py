"""
Este módulo proporciona una función para mostrar el inventario del jugador en la terminal.
Funciones:
    - show_inventory(state: dict) -> None: Muestra el inventario del jugador en la terminal.
El diccionario de estado debe incluir las siguientes claves:
"""
from utils import clear, center_text

def show_inventory(state: dict) -> None:
    """
    Muestra el inventario del jugador en la terminal.
    Args:
        state (dict): Un diccionario que contiene el estado del jugador. 
                      Debe incluir las siguientes claves:
                      - "has_sword" (bool): Indica si el jugador tiene una espada.
                      - "has_key" (bool): Indica si el jugador tiene una llave.
                      - "has_potion" (bool): Indica si el jugador tiene una poción.
                      - "health" (int): La salud actual del jugador (0-100).
    Returns:
        None
    """
    sword: str = "Sí" if state["has_sword"] else "No"
    key: str = "Sí" if state["has_key"] else "No"
    potion: str = "Sí" if state["has_potion"] else "No"
    health: str = str(state["health"]) if state["health"] == 100 else str(
        state["health"]) + " "

    # Limpiar la pantalla.
    clear()
    inventory = rf"""
            \ ||| /
            ( o o )
 ~~~ooO~~~~~~ (_) ~~~~~~~~~~~~
|                             |
|          INVENTARIO         |
|          ~~~~~~~~~~         |
|                             |
|         Espada = {sword}         |
|         Llave = {key}          |
|         Poción = {potion}         |
|                             |
|         Salud = {health}%        |
|                             |
 ~~~~~~~~~~~~~~~~~~~~~~~ooO~~~
          |____|____|
            ||   ||
           ooO   Ooo
"""
    print(center_text(inventory))
    input("Presione ENTER para continuar...")
    print()
