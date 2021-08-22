# indent
# naming convention
if(True):
    pass
else:
    pass  # returns nothing

# looping:
# function():
# class:

# numeric: int, float
# string: (letter, word, sentence)
# - single line commentation
''' 
multi
line
commentation
'''
# str, str(), immutable
# name = "Sachien"
# name = name + "Tendulkar"
fname = "Python dont't \
follows complete C procedure \
it has its own"
lname = 'Y'
comment = """ 
multi
line
commentation - passage couldn't
"""
print(fname, lname)
print(type(comment))  # <class 'str'>

string = "Python Programing"  # character array - indexing (forward, backward)
print("First letter: ", string[0])
print("second letter: ", string[1])
print("third letter: ", string[2])

print("last letter: ", string[-1])
print("previous last letter: ", string[-2])

for i in string:  # for(int i = 0; i<=n; i++); foreach loop
    # print(i)
    pass


fname = "Praveen"
lname = "Kumar"
print(fname, lname)
# direct print
print("My name is ", fname, lname)
# formatting strings
print("My first name %s and second name %s" % (fname, lname))
# format()
print("My first name {} and second name {} and age {}".format(fname, lname, 28))
# ''.format()

# capitalize() - "praveen kumar" - "Praveen kumar"
# lower() - email username --->
# upper()
# endswith() -
# isalpha()
# isdigit()
# isidentifier()
# count() - "Praveen".count('e') ==> 2
exist_email = "pravileaf"
print(exist_email.isalpha())  # True
exist_password = "PrAvEeN@2692"
print(exist_password.isalnum())  # True

# email = input("Enter your email id: ")
# password = input("Enter your password: ")
# if (exist_email == email.lower() and exist_password == password):
#     print("Successfully logged in.......")
# else:
#     print("Entered wrong email/password")

# TRAI rules
# 1--> emergency; 2-5 ---> landline; 6-9 ---> mobile
# also it takes exactly 10 digits

# number = input("Enter the number to check its status: ")
number = "90"

if((number.startswith('6') or number.startswith('7') or
        number.startswith('8') or number.startswith('9')) and
        len(number) == 10):
    print("Yes!, It meets indian mobile standard")

elif((number.startswith('2') or number.startswith('3') or
      number.startswith('5') or number.startswith('5')) and
     len(number) == 8):
    print("Yes!, It meets indian landline standard")

elif(number.startswith('1') and len(number) == 3):
    print("Yes!, It meets indian emergency standard")

else:
    print("Ooops!....No it is not indian number....")


# slicing: string[start: stop: step(optional)]
# audio ---> ringtones; 240s ---> 30s ringtone
# "praveen" ---> "ave"
name = "praveen kumar"
print(name)
print(name[0])
print(name[0:13:1])  # print(name[0:7])
print(name[2:7:1])   # print(name[2:5])
print(name[0:13:2])  # output: paenkmr
print(name[::-1])    # reverse the index
