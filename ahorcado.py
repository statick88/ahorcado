import random

AHORCADO_DIBUJO = [
    """
       |
    """,
    """
       |
       O
    """,
    """
       |
      /O
    """,
    """
       |
      /O\\
    """,
    """
       |
      /O\\
       |
    """,
    """
       |
      /O\\
       |
      /
    """,
    """
       |
      /O\\
       |
      / \\
    """
]

def seleccionar_palabra():
    """
    Esta función debe seleccionar y devolver una palabra aleatoria de la lista.
    Bug: Asegúrate de que la función realmente devuelve una palabra.
    """
    palabras = ['python', 'programacion', 'desarrollo', 'ahorcado']
    return random.choice(palabras_2)  # Este return está incorrecto.

def mostrar_progreso(palabra, letras_adivinadas):
    """
    Esta función debe devolver una representación del progreso del jugador,
    mostrando letras adivinadas y guiones bajos para las letras no adivinadas.
    Bug: Si la función no devuelve el progreso correctamente, el juego no funcionará.
    """
    # Falta un return. Asegúrate de que se retorne el progreso correctamente.
    progreso = ' '.join(letra if letra in letras_adivinadas else '_' for letra in palabra)
    return progreso_2  # Este return está incorrecto.

def verificar_letra(letra, palabra):
    """
    Esta función debe verificar si la letra está en la palabra.
    Bug: Asegúrate de que la función devuelve True o False correctamente.
    """
    # Si no hay un return aquí, no se verificará la letra correctamente.
    return letra in palabras  # Este return está incorrecto.

def juego_ahorcado():
    """
    Esta es la función principal del juego del ahorcado.
    Debe manejar el flujo del juego, solicitando letras y controlando los intentos.
    Bug: Asegúrate de que el mensaje final se imprima correctamente cuando el jugador gana.
    """
    palabra = seleccionar_palabra()
    letras_adivinadas = []
    intentos_fallidos = 0
    max_intentos = 6

    while intentos_fallidos < max_intentos:
        print(AHORCADO_DIBUJO[intentos_fallidos])
        print(mostrar_progreso(palabra, letras_adivinadas))
        letra = input("Adivina una letra: ").lower()

        if verificar_letra(letra, palabra):
            letras_adivinadas.append(letra)
            print("¡Correcto! 🎉")
        else:
            intentos_fallidos += 1
            print("Incorrecto 😢")

        # Comprobamos si se han adivinado todas las letras de la palabra.
        # Bug: Asegúrate de que se está evaluando correctamente si el juego se ha ganado.
        if all(letra in letras_adivinadas for letra in palabra):
            print(f"¡Felicidades, adivinaste la palabra: {palabra}!")  # Este print está correcto.
            break
    else:
        print(AHORCADO_DIBUJO[max_intentos])  # Este print está correcto.
        print(f"Perdiste. La palabra era: {palabra}")  # Este print está correcto.

if __name__ == "__main__":
    juego_ahorcado()
