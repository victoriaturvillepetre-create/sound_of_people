from colorama import Fore

def colour(c):
    return getattr(Fore, c.upper(), "")

class Animal:
    SOUNDS = {
        "duck": "quack",
        "fish": "blub",
        "aaran": "kazam!",
        "martin": "brom",
        "william": "yap",
        "maryam": "67",
        "evelyn": "yay",
    }

    def __init__(self, name, animal, age, colour):
        self.name = name
        self.animal = animal
        self.age = age
        self.colour = colour

    def speak(self):
        sound = self.SOUNDS.get(self.animal)

        if sound is None:
            print(f"{self.name} is not defined as a {self.age} year old {self.colour} {self.animal}")
            return

        print(f"{self.name} is a {self.age} year old {self.colour} {self.animal}")
        for _ in range(self.age):
            print(colour(self.colour) + sound + colour("reset"))

class Aaran(Animal):
    def __init__(self, animal, age, colour):
        super().__init__("Aaran", animal, age, colour)

class Martin(Animal):
    def __init__(self, animal, age, colour):
        super().__init__("Martino", animal, age, colour)

class William(Animal):
    def __init__(self, animal, age, colour):
        super().__init__("William", animal, age, colour)

class Maryam(Animal):
    def __init__(self, animal, age, colour):
        super().__init__("Maryam", animal, age, colour)

class Evelyn(Animal):
    def __init__(self, animal, age, colour):
        super().__init__("Evelyn", animal, age, colour)

def create_animal(cls):
    animal = input(f"What animal is {cls.__name__}? ").lower()
    age = int(input(f"How old is {cls.__name__}? "))
    colour = input(f"What colour is {cls.__name__}? ")

    obj = cls(animal, age, colour)
    obj.speak()

people = [Aaran, Martin, William, Maryam, Evelyn]

while True:
    for person in people:
        create_animal(person)

    if input("Continue? (y/n): ").lower() != "y":
        break
