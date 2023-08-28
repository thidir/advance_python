from functools import reduce
#subtract
def subtract(x,y):
    return x - y
numbers =[20,10,5,1]
print(reduce(subtract,numbers))

#addition
def add(x,y):
    return x + y
number =[20,10,5,1]
print(reduce(add,number))

#divide
def divide(x,y):
    return x / y
me =[20,10,5,1]
print(reduce(divide,me))

