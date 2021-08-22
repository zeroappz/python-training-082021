# julia -
#
'''
void function(){
    x = x+ 100
    y = x + 100
    ....
    print("dfksfoijwof")
}

int function(){
    x = x+ 100
    y = x + 100
    ....
    return 10
}


# int a = 10
# type, address, {}

# stack or function frame

memory will be created at the time of function call (invoke)
at the end of function definition memory will be flushed out

'y' - local scope


return - we can collect particular data from a function

# efficient in terms of memory as well as performance
'''
# non returned
# returned
# length = len('9047048344')
# if length == 10:
#     print("it is indian std mobile number...")

# empty = []
# result = empty.append('name')
# print("Append doesn't return: ", result)  # non-return

# result = empty.pop()
# print("Returned value from pop(): ", result)  # returned function


'''
1) def 
2) naming convention (recommended)
3) comments (recommended)
'''


def function_name():  # function definition; non returned
    print("inside a function....")
    x = 10 * 10
    listData = []
    for i in range(10):
        listData.append(i)
    # print("List value: ", listData)
    # print("function is about to close....")  # memory flush
    return 18  # flush


# invoke
# print('what it returns: ', function_name())
result = function_name()
# print("result: ", result)  # result:  None

# result:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def getAge():
    # age = int(input('Enter your age: '))
    age = 18
    return age


result = getAge()

if result >= 18:
    pass
    # print("you are an adult..")
else:
    pass


def collect_userData():
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    mobile = input('Enter your mobile: ')

    register_form_tile = ["name", "email", "mobile"]  # static keys
    reg_form_value = [name, email, mobile]

    userData = dict(list(zip(register_form_tile, reg_form_value)))
    return userData


# sneha = collect_userData()
# praveen = collect_userData()
# deepak = collect_userData()


stud_list = dict()
for i in range(3):
    result = collect_userData()
    stud_list.update(result)

print('Total students list:', stud_list)
