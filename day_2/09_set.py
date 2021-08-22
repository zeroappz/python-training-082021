# set mathemetics ---> Algebra
# union, intersection, difference, symm-diff
listData = [10, 10, 2, 3, 4, 45, 6, 37, 7, 6]
listData.sort(reverse=True)  # optional parameter
# print(listData)

# indexing ---> each index holds some memory and value (array)
# hashing technique  ---> it checks for the existing data; nearby value

setConversion = set(listData)
# str(), float(), int(), chr(), ascii(), bytes(), set(), tuple(), list(), dict()
# explicit type conversion
# implicit type conversion
# int(input()) ---> 10 # str()

# print(setConversion)  # {} - set

setObj = {0, 1, 2, 1, 0, 2}
# print(setObj, type(setObj))

# add() - append()
# update() - extend()

setObj.add(1)
# # print("after adding value: ", setObj)
setObj.update([4, 5, 6, 7, 8, 9, 0])
# # print("updated value in set: ", setObj)


# union
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}

obj = set_1.union(set_2)
print('After union: ', obj)

obj = set_1.intersection(set_2)
print('After intersection: ', obj)

obj = set_1.difference(set_2)
print('After difference: ', obj)

obj = set_1.symmetric_difference(set_2)
print('After sym difference: ', obj)


# frozenset - immutable
cities = set(["chennai", "trichy", "salem"])
cities.add("coimbatore")

# froze = frozenset(cities)
# froze.add("Madurai")

cities.clear()
# cities.remove("chennai") # keyError
cities.discard("chennai")  # None
if cities.discard("chennai"):
    print("Chennai has already been removed")
else:
    # cities.remove("chennai")  # keyError
    print("Chennai removed successfully....")


# remove(), discard(), union, add, update, clear, difference, intersection
# pop, issuperset,issubset, isdisjoint
a = {'a', 'b', 'c', 'd', 'e'}
b = {'f', 'g'}
print(a.issuperset(b))
print(b.issubset(a))
print(a.isdisjoint(b))
