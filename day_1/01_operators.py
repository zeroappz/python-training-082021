# Comparision operators ---> == , >, < , >=,!=
# Assignment Operators ---> =, +=, -=, *=, **=, /=, //=, %=

import time
a = 10
# b = a + 10  # 20

a = a + 10  # a ===> 20 ---> 5 steps * 500000 ==> 2500000
# print('normal operator: ', a)
a += 10  # output remains same ---> 3   ===> 1500000
# print('assignment operator: ', a)

list = []
start = time.time()  # nano seconds

for i in range(100000):  # 0, 9
    list += [i]  # 3 steps

end = time.time()  # nano secondsclearclear
print("Shorthand Time Taken: ", end-start)

list = []
start = time.time()  # nano seconds

for i in range(100000):  # 0, 9
    list = list + [i]

end = time.time()  # nano seconds
print("Normal Operator Time Taken: ", end-start)
