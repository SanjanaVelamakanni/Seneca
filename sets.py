#sets-unordered,unchangable,doesnt allow duplicates
myset={"hi","hai","hello",True,1,7} 
#true and 1 are considered same
print(myset)
print(len(myset))

#creation of set
set2=set(("python",2))
print(set2)

#accessing items in sets
for i in myset:
    print(i)

#adding
myset.add("java")
print(myset)

#add sets
#update method adds any iterable objects(tuples,dict,list)
myset.update(set2)
print(myset)

#del,remove,discard,clear items from set
myset.remove("hi")
print(myset)
myset.discard("hai")
print(myset)
set2.clear()
print(set2)

#joining sets
set={"helo"}
set1={"bye"}
set3=set1.union(set)
print(set3)

#intersection
a={"apple","banana"}
b={"banana","orange"}
c=a&b #a.intersection(b)
print(c)




