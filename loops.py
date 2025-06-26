#while
i=0
while i<6:
    print(i)
    i+=1

#break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 

#continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#while else
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#for loop
for i in "python":
  print(i)


#break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
#continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#range
for x in range(6):
  print(x)

for x in range(2,6):
  print(x)

for x in range(2,30,3):
  print(x)

adj = ["red", "yellow", "small"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

