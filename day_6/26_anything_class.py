class UserDataAccess(object):
    def __init__(self, name, email, mobile):
        self.name = name
        self.email = email
        self.mobile = mobile

    def collect_userData(self):
        register_form_tile = ["name", "email", "mobile"]  # static keys
        reg_form_value = [self.name, self.email, self.mobile]
        userData = dict(list(zip(register_form_tile, reg_form_value)))
        return userData


sneha = UserDataAccess("Sneha", "sneha@gmail.com", "9047048344")  # instance
result = sneha.collect_userData()

praveen = UserDataAccess(
    "Praveen", "pravileaf@gmail.com", "9047048344")  # instance
result = sneha.collect_userData()

deepak = UserDataAccess("Deepak", "deepak@gmail.com", "9047048344")  # instance
result = sneha.collect_userData()


# stud_list = dict()
# for i in range(3):
#     result = collect_userData()
#     stud_list.update(result)

# print('Total students list:', stud_list)
