# comprehension of list
x = [x for x in range(10)]
print(x)

# anonymous function
# lambda also returns as like as function return
# minimal process can be done using lambda
# lambda argumets: expression
''' out = lambda x, y, z: x*y*z '''


def output(x, y):
    return x*y


x, y = 10, 5
res = output(x, y)
# print('output: ', res)

# print(lambda x, y, z: x*y*z)
# print(lambda x, y: x+y)
# print(lambda x, y: x/y)

'''
zip(), enumerate(), map() & filter() -----> list(); next()
'''

# map(lambda_fun, obj)
# map() - is used to compare objects; returns BOOLEAN value
number = [1, 2, 3, 4, 5, 6]  # i % 2 == 0
new_list = list(map(lambda x: (x % 2 == 0), number))
print('value of map with lambda: ', new_list)


# filter() - is used to compare objects; returns matched value
number = [1, 2, 3, 4, 5, 6]  # i % 2 == 0
new_list = list(filter(lambda x: (x % 2 == 0), number))
print('value of filter with lambda: ', new_list)


def square_val(x):
    return x**2

# square_val = lambda x : x**2


print(square_val(2))
print(square_val(4))
