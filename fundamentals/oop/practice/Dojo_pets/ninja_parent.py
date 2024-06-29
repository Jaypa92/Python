from pets_child import Pets


class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()

    def feed(self):
        self.pet.eat()

    def bathe(self):
        self.pet.noise()
if __name__ == "__main__":


    ninja_1 = Ninja("Yoshi", "Origato", Pets("Buddy", "Lab", "roll over", 100, 100), "bones", "purina")
    print(ninja_1.pet)
    ninja_1.bathe()
    ninja_1.walk()
    ninja_1.feed()
    print(ninja_1.pet.health)
    print(ninja_1.pet.energy)