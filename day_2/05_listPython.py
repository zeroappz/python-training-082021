# list - indexing (forward (0), backward (-1))
# mutable - manipulation
# list supports any kind of data
# it has its own functions (class)

# x = list()
import sys
import time  # system module
# listData = []
# print(sys.getsizeof(listData), id(listData), type(listData))

# append(obj)
# listData.append(1)
# listData.append(2)
# listData.append(3)

# extend(list)
# listData.extend([4, 5, 6, 7, 8, 9])
# print(listData)

list = []
start = time.time()  # nano seconds
for i in range(100000):  # 0, 9
    list += [i]  # 3 steps
end = time.time()  # nano secondsclearclear
print("Shorthand Time Taken: ", end-start)


list = []
start = time.time()  # nano seconds
for i in range(100000):
    list.append(i)
end = time.time()  # nano seconds
print("Time Taken for append(): ", end-start)

list = []
start = time.time()  # nano seconds
for i in range(100000):  # 0, 9
    list = list + [i]
end = time.time()  # nano seconds
print("Normal Operator Time Taken: ", end-start)
