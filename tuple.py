#creation of tuples:
mytuple = ("python","css","java", "c","mysql","html")
print(mytuple)
print(len(mytuple))

tup2 = ("python",)#tuple
print(type(tup2))

nottup = ("python")#str
print(type(nottup))

a = (("a",20,50.90))#also a tuple
print(a)
print(type(a))

#indexing:
print(mytuple[0])
print(mytuple[-1])#negative indexing
print(mytuple[2:4])#accesing range of elements
print(mytuple[3:])
print(mytuple[:-3])
x = mytuple.index("c")
print(x)

#searching in a tuple:
if "python" in mytuple:
  print("element is present")
else:
  print("element not found")
  
#updating:
b = list(mytuple)
b[-1] = "css"
mytuple = tuple(b)
print(mytuple)  

#adding:
b = list(mytuple)
b.append("css")
mytuple = tuple(b)
print(mytuple) 

#removing:
b = list(mytuple)
b.remove("css")
mytuple = tuple(b)
print(mytuple)

#count:
num = mytuple.count("css")
print(num)

#deleting:
del mytuple
print(mytuple)#raises error