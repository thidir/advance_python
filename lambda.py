me=lambda x,y: x+y
print(me(10,20,))


items = [1, 2, 3, 4, 5]
squares = map((lambda x: x ** 2), items)
print(list(squares))