#%%
# declaring a class to create objects with the same props or attributes
class ClassName:
    price = 124
    def __init__(self,mat): # to enable objectName.property thingy
        self.material = mat # so the attribute will be equal to the value assigned to 'mat' var
    
    def printHammer(self):
        print("Hello, I'm from ", self.material)

#notes
# methods -> functions in class
# attributes -> variables in class


# to create an object, just make a name and equal the classname 
newObject = ClassName("Wood")

# to access a property, if you want to print it
# print(objName.propName)
print(newObject.price)

# to access a function inside a class
# objName.function()
newObject.printHammer()

# print out attributes
print(newObject.material)

#%%
# make a class that print out the area of a rectangle
class Rect:

    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length**2
    
bob = Rect(5)
print(bob.area())
# %%
# a class with multiple attributes and a method
class tri:

    def __init__(self, height, length):
        self.height = height
        self.length = length
    
    def area(self) -> int:
        return 0.5*self.height*self.length # for methods, don't use the var (var) but use the attribute (obj.var)
    
adam = tri(6,3)
print(adam.area())

# %%
# Lambda function
# a one line for loop, one time use
# can have multiple arg, but only one expression

funcName = lambda a : a * 2
# a will be the parameter, and a * 2 will be expression that will be executed
# how to run it?
print(funcName(4))
# %%
# use lambda in a function
def myFunc(n):
    return lambda x : x*n

timesTwo = myFunc(2) # this will make timesTwo a function that will return x*2 from the lambda, since n is 2
timesThree = myFunc(3) # will set timesThree to have the lambda function with the expression x*3, since n is 3

# run both functions
print(timesTwo(3)) # a in lambda function will be equal to 3, assigned from this function
print(timesThree(6)) # a = 6
# %%
from functools import reduce 

# this has double lambda
# first -> lambda with param n and will run reduce()
# second -> lambda with x and _ -> will run x+[x[-1]] + x[-2]]
# fib = lambda n: reduce(lambda x, _: x+[x[-1] + x[-2]], range(n-2), [0,1])

# print(fib(5))

my_list = [5, 4, 3, 2, 1]
print(reduce(lambda x, y: x + y, my_list,4))
# %%
