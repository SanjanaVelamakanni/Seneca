class Bird:
    def fly(self):
        print("Some birds can fly")

class Parrot(Bird):
    def fly(self):
        print("Parrot flies high")

class Ostrich(Bird):
    def fly(self):
        print("Ostrich can't fly")

# Looping over different objects
for bird in [Parrot(), Ostrich()]:
    bird.fly()
