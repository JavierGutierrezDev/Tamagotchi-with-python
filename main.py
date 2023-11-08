from tamagotchi import Tamagotchi, clear_screen
import threading

def main():
    pet_name = input("¿Cómo quieres nombrar a tu Tamagotchi? ")
    pet = Tamagotchi(pet_name)

    print(f"{pet.name} ha nacido!")
    pet.show_mood()

    pet.live_thread = threading.Thread(target=pet.live)
    pet.live_thread.start()

    try:
        while pet.alive:
            clear_screen()  # Limpiar la pantalla antes de imprimir el estado actual

            pet.check_status()  # Imprime el estado del Tamagotchi

            # Explicar que las opciones se pueden elegir por su inicial.
            print("¿Qué te gustaría hacer?")
            print("[A]limentar, [J]ugar, [P]ersonalizar, [S]alir")
            action = input().strip().lower()[0]  # Toma solo el primer carácter y lo convierte a minúscula

            if action == "a":
                pet.feed()
            elif action == "j":
                pet.play()
            elif action == "p":
                pet.customize()
            elif action == "s":
                print("Gracias por jugar.")
                pet.stop()
                break
            else:
                print("Acción no reconocida. Inténtalo de nuevo.")

    finally:
        pet.stop()
        pet.live_thread.join()

if __name__ == "__main__":
    main()
