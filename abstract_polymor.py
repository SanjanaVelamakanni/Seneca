#Abstract class
class Animal:
    pass

class Dog(Animal):
    def make_sound(self):
        print("Dog says: Woof!")
        
class Cat(Animal):
    def make_sound(self):
        print("Cat says: Meow!")


dog = Dog()
dog.make_sound()  

cat = Cat()
cat.make_sound()

#polymorphism
class Add:
  def hi(self, a, b):
    self.a = a
    self.b = b
    print(a+b)


add1 = Add()
add1.hi(1,2)

add2 = Add()
add2.hi("hi","hello")