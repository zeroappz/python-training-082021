print('Good Morning......')  # pre-loaded

# Functional & Object oriented

# Mech - 50 (mech.xls)
# Civil - 50
# CSE - 50

# 45kb for 3 (memory) - 15sec (Time)
# civil.dinesh
# mech.praveen
# 150


# Pythontraining.xls - cse, mech, civil - efficient
# 35kb for 1(memory) - 5sec (Time) -----> Preferable

# file.mech.praveen
# file.civil.dinesh


'''
class ClassName{
    void main(){
        printf("");
    }
}
PUBG - shooting game:
1. Snipper - 8bullets - firing - reloading: snipper.reload(8)
2. Pistol  - 30bullets - firing - reloading: pistol.reload(30)

OOPs - Object Oriented Paradigm(s)
'''
# object - supermost class of a progam

# object - global functions, keywords,filepath, error classes

# Static programming & Dynamic Programming - primary factor
#
# int num = 10;     4/8bytes - address (0x4564987) - 1010 (binary) - 4bits
# 5000int; 5000*4 ==> 20000bytes ----> 20bytes

# left to right - static
# right to left - dynamic programming

number = 90470.50
test = number
print('Address and type of number: ', id(number), type(number))  # address
print('Address and type of 90470: ', id('90470'), type('90470'))  # address
print('Address and type of test: ', id(test), type(test))  # address

number = "Praveen"  # duplicate object
print('Address and type of number: ', id(number), type(number))  # address
# memory sharing, value sharing

'''
1. Dynamic prog
2. OOPs
3. Wide Application development - webscript, application
4. Community Support
5. Easy to learn
'''
# ASCII - English - a-z; A-Z, 0-9, %^$&* => 128values, 256 Extended
# UTF - Unicode (64) ---> Tamil,

# a (Human) - 95 - 0101010 (ML) - ASCII procedure
# 0x0000 - 0101101
# tamil_first_character = '\u00e9' + '\u00e8'
# print('First letter in Tamil is: ', tamil_first_character)

# keywords - 33 Python & identifiers
# variable
mobile_number = "9047048344"
# Types of data - numeric (int, float, imaginary), string (string)
# list = [1, 2.5, 'a', "praveen"]

# Operators
# Arithmetic - *, /, +, -, %, // (floor division), **
a = 10
b = 25
print('Division: ', 10/3)
print('Floor division: ', 10//3)  # quotient, % reminder
print('power: ', 10**2)  # pow(10, 2)

# logical operators
# &&, ||, ^, !
# True && True ==> True
# if (email || mobile) True


# and, or, not
exist_username = "pravileaf"
exist_email = "pravileaf@gmail.com"
exist_password = "Restricted"

email = input("Enter your email: ")
password = input("Enter your pwd: ")
username = input("Enter your username: ")

if ((exist_email == email.lower() or exist_username == username) and
        exist_password == password):
    print("Successfully logged in.......")
    # indentation
else:
    print("Entered wrong email/password")


voterID = True
age = 28
if(voterID == True and age >= 18):
    print("eligible to vote")
else:
    print("not eligible go away....")


# membership operators: in, not in
# Identity Operators: is, is not
a = 10
b = 20
if(a is not b):
    print("yes it is there!!")
else:
    print("no it is not!!")

print('o' in "Praveen")  # True
