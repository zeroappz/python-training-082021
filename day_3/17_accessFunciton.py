# import functions
# import functions as f
from functions import *

# from time import time, sleep

# package

# print("before function call....")
# functionCheck()
# brandList()
# print("after function call....")


# categories = f.categoryList()
# brands = f.brandList()
# products = f.productsList()

# print("Total available category: ", categories)
# print("Total available brands: ", brands)
# print("Total available products: ", products)


for i in range(10):
    addUserDetails(i)

result = getUserDetails()
print("Total users list: ", result)
deleteUserDetails(2)
# deleteAll()


'''
{
    1: ['Deepak', 'test1', '97987'],
    2: ['sneha', 'sneha', '897941'],
    3: ['praveen', 'fdsfjoi', '79799']
}
'''
