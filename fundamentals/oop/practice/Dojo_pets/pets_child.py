class Pets:

    pet_available = []

    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        Pets.pet_available.append(self)

    def sleep(self):
        self.health = self.health + 25

    def eat(self):
        self.energy = self.energy + 5
        self.health = self.health + 10

    def play(self):
        self. health = self.health + 5

    def noise(self):
        if self.type == "dog":
            print("bark, bark")
        elif self.type == "cat":
            print("meow, hiss")

if __name__ == "__main__":

    buddy = Pets("Buddy", "dog", "Roll over", 100, 100)
    print(buddy.health)

    print(Pets.pet_available)
