mylist=["python","java","c","js",8]
print(mylist)
print(len(mylist)) #lengthoflist
print(type(mylist))
print(mylist[1]) #accessing
if "c" in mylist:
    print("c is in the list")
mylist[1]="html"
mylist.insert(2,"java")
mylist.append("hai")
list2=["ok"]
mylist.extend(list2)
mylist.remove("java")
mylist.pop()
#listcomprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist) 
num=[2,6,1,9,4]
num.sort() #sortlist
print(num)
num.sort(reverse=True) #descending
print(num)
num2=num.copy() #copy
print(num2)
num3=num+num2 #joining
print(num3)
#listmethods
num3.clear()
print(mylist.index("js"))