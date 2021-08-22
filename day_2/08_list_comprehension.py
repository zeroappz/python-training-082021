# even simplyfing the data storage
listObj = []

for i in range(0, 101):  # range(), condition, append(), i
    if i % 2 == 0:
        listObj.append(i)

# print(listObj)

# comprehension
# [value : for_loop]
compObj = [i for i in range(100)]  # append()
# print(compObj)

# [value : for_loop : condition]
compObj = [i for i in range(101) if i % 5 == 0]
# print(compObj)

# [value(exp) : for_loop]
compObj = [i*i for i in range(10) if i % 2 == 0]
# print(compObj)

# [value(exp) : for_loop : for_loop : condition]
compObj = [i+j for i in [10, 20, 30] for j in [5, 15, 25]]
print(compObj)

output = []
for i in [10, 20, 30]:
    for j in [5, 15, 25]:
        output.append(i+j)

print(output)


# list comprehension is far better than append()
