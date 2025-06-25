#creating a dictionary:
#using flower braces:
mydict = {
  "brand": "porsche",
  "model": "gt3 rs",
  "year": 2001
}
print(mydict)

#using method:
mydict2 = dict(brand= "Ford",model= "Mustang",year=1964)
print(mydict2)

#accesing:
x = mydict["brand"]
print(x)
y = mydict2.get("brand")
print(y)

#keys:
key = mydict.keys()
print(key)

#values:
val = mydict.values()
print(val)

#update:
mydict.update({"year":2025})
print(mydict)

#adding:
mydict["color"] = "blue"
print(mydict)

#removing:
mydict.popitem()#removes last item
print(mydict)
mydict.pop("year")#removes using the key
print(mydict)

#looping keys:
for i in mydict:
  print(i)
  
#looping values:
for i in mydict:
  print(mydict[i])
  
#looping both:
for i,j in mydict.items():
  print(i, ":" ,j)
  
#copy:
newdict= mydict.copy()
print(newdict)

#deleting:
del mydict
print(mydict)#error