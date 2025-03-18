"""
Este módulo proporciona varias utilidades para la manipulación de la consola y 
la interacción con el usuario.
Funciones:
- clear(): Limpia la consola.
- print_slowly(texto, velocidad): Imprime el texto dado en la terminal un carácter a 
  la vez con un retraso.
- center_text(texto): Centra el texto en la consola.
- get_choice(opciones): Muestra una lista de opciones y solicita al usuario que haga una elección.
"""
import os
import time


def clear() -> None:
    """Limpia la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_slowly(text: str, speed: float = 0.03) -> None:
    """
    Imprime el texto dado en la terminal un carácter a la vez con un retraso.

    Args:
        text (str): El texto a imprimir lentamente.
        speed (float, optional): El retraso en segundos entre cada carácter. 
        El valor predeterminado es 0.03 segundos.

    Returns:
        None
    """
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()


def center_text(text: str) -> str:
    """ Centra el texto en la consola.
    Args:
        text (str): El texto a centrar.

    Returns:
        str: El texto centrado.
    """
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    console_width = os.get_terminal_size().columns
    padding = (console_width - max_length) // 2
    centered_lines = [f"{' ' * padding}{line}" for line in lines]
    return '\n'.join(centered_lines)


def get_choice(options: list[str]) -> int:
    """
    Muestra una lista de opciones y solicita al usuario que haga una elección.

    Args:
        options (list[str]): Una lista de cadenas que representan las opciones disponibles.

    Returns:
        int: El índice (basado en 1) de la opción elegida.

    La función solicitará repetidamente al usuario hasta que se haga una elección válida.
    """
    while True:
        for i, option in enumerate(options, 1):
            print(f"{i} - {option}")

        choice = input("\n¿Qué deseas hacer? > ")

        if choice.isdigit() and int(choice) >= 1 and int(choice) <= len(options):
            return int(choice)
        print("Opción no válida. Intenta de nuevo.\n")
