class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating objects
dog1 = Dog("Buddy", "Labrador")
dog2 = Dog("Tommy", "Beagle")

# Accessing methods
dog1.bark()   # Output: Buddy says Woof!
dog2.bark()   # Output: Tommy says Woof!
