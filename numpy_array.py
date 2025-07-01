from numpy import *
arr=array([1,2,3,4,5])
print(arr)
print(arr.dtype)

arr1=linspace(0,15,16)
print(arr1)

arr2=arange(1,15,2)
print(arr2)

arr3=logspace(1,20,5)
print(arr3)

a=ones(5)
b=zeros(5)
print(a)
print(b)

#vectorized operation
arr4=array([1,2,3,4,5])
ar=arr4+5
print(ar)

arr5=array([5,4,3,2,1])
arr6=arr4+arr5
print(arr6)

#mathematical operations on array
print(sin(arr4))
print(log(arr4))
print(sqrt(arr4))
print(min(arr4))
print(max(arr4))
print(sum(arr4))

#copying an array
aar=array([3,2,5,7,9])
aae=aar
print(aar)
print(aae)
print(id(aar))  #aliasing
print(id(aae))  #stores in same address


#shallow copy
aad=aar.view()
aar[1]=1
print(aar)
print(aad)
print(id(aar))
print(id(aad))

#deep copy
are=aar.copy()
aar[1]=3
print(aar)
print(are)
print(id(aar))
print(id(are))

