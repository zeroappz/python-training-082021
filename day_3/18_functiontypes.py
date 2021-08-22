# def function()
# def function(param):
# overloading, overriding
# no restrictions with parameters

''' zero param '''
''' parameterized function '''


def newFunction(listObj, n):  # pass by reference
    # # print('inside func: ', id(listObj))
    # del listObj[0]
    for i in range(n+1, 31):
        listObj.append(i)


listObj = [1, 2, 3, 4, 5, 6]
# # print('outside func: ', id(listObj))
newFunction(listObj, len(listObj))
# # print(listObj)


def newFunction(listObj):  # pass by reference
    # # print('inside func: ', id(listObj))
    # del listObj[0]
    for i in range(7, 21):
        listObj.append(i)


listObj = [1, 2, 3, 4, 5, 6]
# # print('outside func: ', id(listObj))
newFunction(listObj)
# # print(listObj)

# reference (implicit pointers)

''' default parameter '''


def farenheit(default=30):
    # print("Current temp is: ", default)
    pass


farenheit()
farenheit(36)  # over-riden


def sort(reverse=False):  # optional parameter; default value in it
    if reverse == False:
        # print("Ascending sort")
        pass
    else:
        # print("Descending sort")
        pass


sort(False)
sort(reverse=True)

'''normal param and default param'''


def testFunc(a, b, c=0, d=0):  # key word arguments
    # print("a:{} and b:{} and c:{} and d:{}".format(a, b, c, d))
    # a:10 and b:20 and c:0 and d:0
    # result = dict([a, b, c, d])
    # # print(result)
    pass


testFunc(10, 20)        # a:10 and b:20 and c:0 and d:0
testFunc(10, 20, 25)    # a:10 and b:20 and c:25 and d:0
testFunc(10, 20, 25, 45)    # a:10 and b:20 and c:25 and d:45

''' Arbitrary Named function '''


def listDataProcess(*data):  # pointer (base value ...... n: 0 - n)
    # print('Data: ', data)
    pass


data = [1, 2, 3, 4, 5]          # packed value
listDataProcess(1)
listDataProcess(1, 2)
listDataProcess(1, 2, 3)
listDataProcess(1, 2, 3, 4)
listDataProcess(1, 2, 3, 4, 5, 6, 7, 8, 9)

listDataProcess(data[0], data[1])
listDataProcess(data[0], data[1], data[2])
listDataProcess(data[0], data[1], data[2], data[3])  # unpacking the values


''' Arbitrary keyword (keyvalue) parameters'''


def keyWordArbitrary(**userData):
    # print('My data: ', userData)
    return userData


keyWordArbitrary(name="Praveen", email="pravileaf", num="9047048344", age="28")
keyWordArbitrary(name="Pavithra", email="pravileaf", num="9047048344")
keyWordArbitrary(name="Sneha", email="pravileaf", num="9047048344")
keyWordArbitrary(name="Deepak", email="pravileaf", num="9047048344")
keyWordArbitrary(name="Subhalaksmi", email="pravileaf", num="9047048344")
keyWordArbitrary(name="priyadarshini", email="pravileaf", num="9047048344")


'''
Functions:
    1) def, commentations, funcitonname
    2) single param, multi parmas
    3) default parameters   - a=10
    4) Arbitrary params - *args
    5) kwargs params    - **kwargs
    6) packing & unpacking
    7) data transfer from one file to another
    8) return, non-return
'''


def func(list):
    for i in range(len(list)):
        print('value is {}'.format(i))  # unpacking


func([1, 2, 3, 4, 5])       # packing

# zip(obj, obj2) ----> upack; (), (), ()
# list(zip(obj, obj2)) ----> packing []


def passDict(obj):
    print(obj)


dictObj = dict(list(enumerate(["apple", "sammy", "huawei"])))
passDict(dictObj)  # passing the dictionary to the function


def passDictKWarg(**obj):
    print(obj)  # unpack - dict pack


passDictKWarg(apple="Apple", sam="Sammy", huawei="Huawei")  # pack
passDictKWarg(apple="Apple", sam="Sammy",
              huawei="Huawei", honor="Honor")  # pack

# normal param
# default argument
# arbitrary (*args) ----> 0 to n parameter
# kwargs (**kwargs) ----> (a=10, b=20) ---> dictionary


# stack frame procedure -----> local scope objects
# return keyword ----> taking the object out
# transfer data from one file to another (n number of files)
