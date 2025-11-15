class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def make_sound(self):
        return "Some generic sound"

    def move(self):
        return "The animal moves"

class Mammal(Animal):
    def __init__(self, name, habitat, has_fur=True):
        super().__init__(name, habitat)
        self.has_fur = has_fur

    def feed_young(self):
        return "Feeds milk to young"

class Bird(Animal):
    def __init__(self, name, habitat, can_fly=True):
        super().__init__(name, habitat)
        self.can_fly = can_fly

    def lay_eggs(self):
        return "Lays eggs"

    def fly(self):
        return "Flies in the sky" if self.can_fly else "Cannot fly"

class Fish(Animal):
    def __init__(self, name, habitat, water_type="freshwater"):
        super().__init__(name, habitat)
        self.water_type = water_type

    def swim(self):
        return "Swims in the water"

    def breathe_underwater(self):
        return "Uses gills to breathe"


lion = Mammal("Lion", "Savannah")
eagle = Bird("Eagle", "Mountains")
salmon = Fish("Salmon", "River", "freshwater")

print(lion.name, "-", lion.make_sound(), "-", lion.feed_young())
print(eagle.name, "-", eagle.fly(), "-", eagle.lay_eggs())
print(salmon.name, "-", salmon.swim(), "-", salmon.breathe_underwater())
