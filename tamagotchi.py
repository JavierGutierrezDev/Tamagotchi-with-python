import sys
import time
import threading
import os
from aspects import get_aspect

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.happiness = 5
        self.health = 5
        self.alive = True
        self.appearance = get_aspect(self.happiness,self.alive) # Default appearance
        self.accessories = None

 

    def feed(self):
        if self.hunger < 10:
            self.hunger += 1
            print(f"Has alimentado a {self.name}.")
        else:
            print(f"{self.name} no tiene hambre.")
        self.show_mood()

    def play(self):
        if self.happiness < 10:
            self.happiness += 1
            print(f"Has jugado con {self.name}.")
        else:
            print(f"{self.name} está muy contento ahora mismo!")
        self.show_mood()

    def check_status(self):
        print(f"Estado de {self.name}:")
        print(f"Hambre: {self.hunger}")
        print(f"Felicidad: {self.happiness}")
        print(f"Salud: {self.health}")
        self.show_mood()
        if self.hunger == 0 or self.happiness == 0 or self.health == 0:
            self.alive = False
            print(f"{self.name} ha dejado de estar con nosotros. :(")

    def show_mood(self):
        print(get_aspect(self.happiness,self.alive,self.accessories))

    def live(self):
        while self.alive:
            clear_screen()
            self.hunger -= 1
            self.happiness -= 1
            self.check_status()
            time.sleep(5)

    def stop(self):
        self.alive = False

    def customize(self):
        print("¡Vamos a personalizar a tu Tamagotchi!")
        print("1. Gato básico")
        print("2. Gato con sombrero")
        print("3. Gato con moño")
        print("4. Gato con gafas")
        print("5. Gato con bufanda")
        print("6. Gato con sombrero de fiesta")

        choice = input("Elige una opción: ")

        if choice == "1":
            self.accessories = None
        elif choice == "2":
            self.accessories = "hat"
        elif choice == "3":
            self.accessories = "bow"
        elif choice == "4":
            self.accessories = "glasses"
        elif choice == "5":
            self.accessories = "scarf"
        elif choice == "6":
            self.accessories = "party_hat"
        else:
            print("Opción no válida, manteniendo la apariencia actual.")
        
        self.show_mood()

    def set_appearance(self, style):
        if style == "basic":
            self.appearance = self.happy_cat
        elif style == "hat":
            self.appearance = self.hat_cat
        elif style == "bow":
            self.appearance = self.bow_cat

        print("¡Apariencia actualizada!")

def clear_screen():
    # Para Windows usa 'cls', para Unix/Linux/Mac usa 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

