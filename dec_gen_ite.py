#decorators
#wraps a function in a function to extend its behaviour
#example
def div(a,b):
    print(a/b)
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div=smart_div(div)
div(2,4)



#iterator
#allows looping one element at a time

#using for loop
nums=[1,2,3,4]
for i in nums:
    print(i)

num=[7,4,2,8]
it=iter(num)
print(it.__next__)
print(next(it))

#create own iterator
class TopTen:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
values=TopTen()
for i in values:
    print(i)


#generators
def TopTen():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1

values=TopTen()
for i in values:
    print(i)
