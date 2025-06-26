class Person:
    def __init__(self,name,age): #constructor "init_"
        self.name = name
        self.age = age
    def welcome(self):#method in a class
        print("Welcome")

#creation of a object
p1 = Person("sanjana",20)

#method calling 
p1.welcome()

#object update
p1.name = "sharma"
print(p1.name)
print(p1.age)