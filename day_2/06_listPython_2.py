# remove(), clear(), del, pop()
listData = ["Praveen", "Sriram", "Niranjani", "Subhalakshmi"]

del listData[0]  # item deletion, entire obj
print("After Item deletion: ", listData)

listData.remove("Sriram")  # ValueError: x not in list
print("After removal: ", listData)

returnedData = listData.pop(-1)  # removes last object
print("popped obj {} remaining list {}".format(returnedData, listData))

print(listData.remove("Niranjani"))

listData.clear()  # flushes the entire data and leaves empty list
print("After clear: ", listData)

# None (null)

# count(), insert(obj, position)

# shopping cart
# [1, 2, 3, 4, 5, 6] ===> [1,5,3] ===> [2, 4, 6]

shopList = ["dairy_milk", "iPhone", "Mac", "Helmet", "Jerkin", "Tablet"]
cart = []

while shopList != []:
    obj = shopList.pop()
    cart.append(obj)

finalCartVal = tuple(cart)
print("My cart value: ", cart)
print("Available shopList: ", shopList)

# slicing
fname = ["Praveen", "Sriram", "Pavithra", "Subhalakshmi"]
print(listData[0:4:2])
print(len(listData))

lname = ["Kumar", "Kumar", "Raja", "Muthukumar"]

fullname = fname + lname
print(fullname)
