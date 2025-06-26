x=lambda a: a+10
print(x(5))

x=lambda a,b:a*b
print(x(2,3))

#lambda in functions
def myfunc(n):
    return lambda a:a*n
mydoubler=myfunc(2)
mytri=myfunc(3)
print(mydoubler(11))
print(mytri(11))

#lambda can take any number of functions but can have only one argument