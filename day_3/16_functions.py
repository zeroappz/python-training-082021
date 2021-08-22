def categoryList():
    '''Adds new category using this funciton...'''
    category = []
    count = 0
    while True:
        add_new = input("Enter new Category name: ")
        category.append(add_new)
        count += 1
        if count == 5:
            # print("stack overflow")
            break
    return category


def brandList():
    '''Adds new brands using this funciton...'''
    brands = []
    count = 0
    while True:
        add_new = input("Enter new Brand name: ")
        brands.append(add_new)
        count += 1
        if count == 5:
            # print("stack overflow")
            break
    return brands


def productsList():
    '''Adds new products using this funciton...'''
    products = []
    count = 0
    while True:
        add_new = input("Enter new Product name: ")
        products.append(add_new)
        count += 1
        if count == 5:
            # print("stack overflow")
            break
    return products


def functionCheck():
    print("Just checkingwhether it works or what...")


userData = dict()  # global object


def addUserDetails(user_id):
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    mobile = input('Enter your mobile: ')
    reg_form_value = [name, email, mobile]
    userData[user_id] = reg_form_value
    # dict['key'] = value
    # print(userData)


def getUserDetails():
    return userData


def deleteUserDetails(user_id):
    del userData[user_id]
    print("After deleting user_id {} the dict is {}".format(user_id, userData))


# def deleteAll():
#     del userData
