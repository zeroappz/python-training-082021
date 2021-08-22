# [ ("praveen", "kumar"), ("sriram", "kumar") ]
# fullname = list(zip(fname, lname))
# print(fullname)
import sys
listData = ["Praveen", "Sriram", "Pavithra", "Subhalakshmi", "Deepak"]
lname = ["Kumar", "Kumar", "Raja", "Muthukumar", "Chahar"]
age = ["28", "20", "20", "20", "20"]
# enumerate
# print(list(enumerate(listData)))  # [ (), (), () ]
# print()
# print(list(zip(listData, lname, age)))


output = [
    ['Praveen', 'Kumar', '28'], ['Sriram', 'Kumar', '20'],
    ['Pavithra', 'Raja', '20'], ['Subhalakshmi', 'Muthukumar', '20'],
    ['Deepak', 'Chahar', '20']
]
output[1][0] = 'Ashok'
print(output[1])

# tuple (immutable) - list (mutable):
# size (lesser in size), non-manipulation, security

# x = tuple()
x, y = (1, 2, 3, 6, 7), [1, 2, 3, 6, 7]
# print(type(x), type(y) )
print(sys.getsizeof(x), sys.getsizeof(y))

# append(), pop(), remove(), insert(), del[0] -
# del x[0]  # tulpe' object doesn't support item deletion
del x

convertListToTuple = tuple(y)  # lesser in size, immutable, faster accessiblity
# del convertListToTuple[0]
# print(convertListToTuple)

# in not in
print("Praveenkumar" in listData)
