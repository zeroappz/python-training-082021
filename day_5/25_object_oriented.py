# object -
# earth is an object
# python - object

# without oops --> debugging
# class GoogleMeet:
#     # listData = [] # class atribute

#     def __init__(self, listData):
#         self.listData = listData

#     def function(self):
#         ''' self is an object - instance specifif function '''
#         ''' method of a class GoogleMeet '''
#         for i in range(10):
#             self.listData.append(i)
#         print("List data: ", self.listData)


# praveen = GoogleMeet()  # instantiation
# praveen.function()

# sneha = GoogleMeet()  # instantiation
# sneha.function()


class StudentsDetails:
    clg_name = "KRGI"  # static or generic value for all instances

    def __init__(self, name, age, dept):  # instance specific data
        self.name = name  # praveen.name  = "Praveen"
        self.age = age
        self.dept = dept

    # instancemethod
    def displayData(self):  # disply user data
        print("My details are: name {}, age {} and dept {} and college name {}"
              .format(self.name, self.age, self.dept, StudentsDetails.clg_name)
              )

    @staticmethod  # annotations
    def function():
        print("it is a function not a method accessed")

    @classmethod
    def functionName(cls):
        print("I am a class method")


def sleep():
    praveen = StudentsDetails("Praveen", "28", "IT")
    praveen.displayData()
    praveen.function()
    StudentsDetails.functionName()  # cls method

    deepak = StudentsDetails("Deepak", "20", "MECH")
    deepak.displayData()
    deepak.function()

    priya = StudentsDetails("Priya", "28", "IT")
    priya.displayData()
    priya.function()

    subha = StudentsDetails("Subha", "20", "MECH")
    subha.displayData()
    subha.function()

    StudentsDetails.functionName()  # cls method


if __name__ == "__main__":  # checking the current file execution
    # print('name of the current file: ', __name__)
    sleep()
