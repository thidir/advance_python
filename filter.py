def is_even(input):
    return input %2==0
numbers = [1,2,3,4,6,8,10]
print(list(filter(is_even , numbers)))

def too_old(x): return x > 30
ages = [22, 25, 29, 34, 56, 24, 12]
print(list(filter(too_old, ages)))