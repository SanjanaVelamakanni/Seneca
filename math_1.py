import datetime
x=datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A")) 
y = datetime.datetime(2018, 6, 1)
print(y.strftime("%B"))

#math lib
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y) 

x = abs(-7.25)
#return positive
print(x)

x = pow(4, 3)
print(x) 

import math
x = math.sqrt(64)
print(x) 
y=math.pi
print(y)

a = math.ceil(1.4)
b = math.floor(1.4)
print(a) # returns 2
print(b) # returns 1

