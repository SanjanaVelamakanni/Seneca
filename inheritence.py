#creation of a class
class Person:
  def __init__(self, name, age):#-->constructor "init_"
    self.name = name
    self.age = age

#inheritence
class Child(Person):
    def _init_(self, name, age):
       super()._init_(name, age) #-->super function used to link the classes
    
#pass and Multiple inheritance
class Dog(Child):
    pass

#creation of a object for a inherted class
p1 = Child("sanjana",20)
p2 = Dog("lab",4)

#object creation
p1.name = "sharma"
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)