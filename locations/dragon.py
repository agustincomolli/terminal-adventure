"""
Este módulo define la función `show_dragon_location` que maneja la interacción del jugador
con un dragón en una ubicación específica del juego. Dependiendo del estado actual del 
jugador, se le presentan diferentes opciones y se actualiza el estado del juego en 
consecuencia.
Funciones:
    - show_dragon_location(state: dict) -> dict: Muestra la ubicación del dragón y permite 
      al jugador tomar decisiones basadas en su estado actual. Devuelve el estado actualizado 
      del juego después de la interacción con el dragón.
Dependencias:
    - random: Para generar probabilidades de éxito en las acciones del jugador.
    - ..utils: Para las funciones `print_slowly`, `center_text` y `get_choice`.
    - ..assets.art: Para la constante `DRAGON` que contiene la representación artística del dragón.
    - ..inventory: Para la función `show_inventory` que muestra el inventario del jugador.
"""
import random
from utils import print_slowly, center_text, get_choice
from assets.art import DRAGON
from inventory import show_inventory

def show_dragon_location(state: dict) -> dict:
    """
    Muestra la ubicación del dragón y permite al jugador tomar decisiones
    basadas en su estado actual.
    Args:
        state (dict): El estado actual del juego, incluyendo la salud del jugador,
                      si tiene la espada antigua, si tiene pociones curativas, y
                      la ubicación actual.
    Returns:
        dict: El estado actualizado del juego después de la interacción con el dragón.
    """
    print(center_text(DRAGON))
    print_slowly("¡Un enorme dragón rojo se alza frente a ti!")
    print_slowly("Sus ojos amarillos te miran fijamente mientras exhala humo " +
                 "por sus fosas nasales.\n")

    if state["has_sword"]:
        options = ["Luchar con la espada antigua", "Huir",
                   "Usar poción curativa", "Revisar tu inventario"]
        choice = get_choice(options)

        if choice == 1:
            print_slowly(
                "¡Empuñas la espada antigua, que comienza a brillar con una luz azul!")
            print_slowly(
                "El dragón retrocede ante el brillo, parece temer a la espada.")
            print_slowly("Avanzas con determinación...")

            # Probabilidad de éxito del 70%
            if random.random() < 0.7:
                print_slowly(
                    "¡Con un movimiento rápido, logras herir al dragón!")
                print_slowly("La bestia ruge de dolor y se retira volando por una " +
                             "apertura en el techo.")
                print_slowly("¡Has derrotado al dragón y el tesoro es tuyo!")
                state["location"] = "exit"
            else:
                print_slowly(
                    "¡El dragón es demasiado rápido y te golpea con su cola!")
                state["health"] -= 50
                print_slowly("¡Has perdido 50 puntos de salud! " +
                             f"Salud actual: {state['health']}")
                if state["health"] <= 0:
                    print_slowly("El golpe es demasiado fuerte...")
                    print_slowly("Todo se vuelve oscuro...")
                    state["location"] = "death"
                else:
                    print_slowly("Te tambaleas pero logras mantenerte en pie.")
        elif choice == 2:
            print_slowly("Intentas huir del dragón...")
            # Probabilidad de éxito del 40%
            if random.random() < 0.4:
                print_slowly("¡Logras escabullirte mientras el dragón está " +
                             "distraído con el tesoro!")
                state["location"] = "right"
            else:
                print_slowly(
                    "¡El dragón te bloquea el paso y te ataca con sus garras!")
                state["health"] -= 60
                print_slowly("¡Has perdido 60 puntos de salud! " +
                             f"Salud actual: {state['health']}")

                if state["health"] <= 0:
                    print_slowly("El ataque es letal...")
                    state["location"] = "death"
        elif choice == 3:
            if state["has_potion"]:
                print_slowly("Bebes rápidamente la poción curativa.")
                state["health"] = min(100, state["health"] + 50)
                print_slowly(
                    f"¡Te has curado! Salud actual: {state['health']}")
                state["has_potion"] = False
            else:
                print_slowly("¡No tienes ninguna poción curativa!")
        else:
            show_inventory(state)
    else:
        print()
        options = ["Intentar huir", "Usar poción curativa",
                   "Revisar tu inventario"]
        choice = get_choice(options)

        if choice == 1:
            print_slowly("Intentas huir del dragón...")
            # Probabilidad baja de éxito sin espada
            if random.random() < 0.2:
                print_slowly("¡Por pura suerte logras escabullirte mientras el " +
                             "dragón está distraído!")
                state["location"] = "right"
            else:
                print_slowly(
                    "¡El dragón te bloquea el paso y te ataca con fuego!")
                state["health"] -= 70
                print_slowly(
                    f"¡Has perdido 70 puntos de salud! Salud actual: {state['health']}")

                if state["health"] <= 0:
                    print_slowly("Las llamas te consumen...")
                    state["location"] = "death"
        elif choice == 2:
            if state["has_potion"]:
                print_slowly("Bebes rápidamente la poción curativa.")
                state["health"] = min(100, state["health"] + 50)
                print_slowly(
                    f"¡Te has curado! Salud actual: {state['health']}")
                state["has_potion"] = False
            else:
                print_slowly("¡No tienes ninguna poción curativa!")
        else:
            show_inventory(state)

    input("\nPresione ENTER para continuar...")
    return state
