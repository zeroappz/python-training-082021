# handle - unhandle
# handling and error or exception leads to control program(application)
# termination


'''
    print(5/0)
    ZeroDivisionError: division by zero

    list = [1, 2]
    print(list[4])
    IndexError: list index out of range

    import times
    ModuleNotFoundError: No module named 'times'

    file = open("Z:\\somefilename.txt")
    FileNotFoundError: [Errno 2] No such file or directory: 'Z:\\somefilename.txt'

    numer = int(input('value for x: '))
    denom = int(input('value for y: '))
    z = numer/denom  # ZeroDivisionError: division by zero
'''


try:
    numer = int(input('value for x: '))
    denom = int(input('value for y: '))
    z = numer/denom  # ZeroDivisionError: division by zero

    list = [1, 2]
    print(list[0])

    import time

    file = open("Z:\\tesla.docx")

except ZeroDivisionError as obj:
    # print("You must enter non-zero value for denominator...")
    print(obj)

except IndexError as obj:
    print(obj)

except ModuleNotFoundError as obj:
    print(obj)

except Exception as obj:
    print(obj)  # supermost exception can handle any error
    # given only at the end; BaseException(object); Exception

print("next line of the program.....")


'''
try:
    pass
except Class as obj:
    pass
except:
    pass
except SuperMostClass as obj:
    pass
'''


# object ----> BaseException ----> Exception ----> TypeError, MNFError, FNFError

# shutdown or restart ----> word, txt, pdf, browser (would you like to close all)
# before shutdown - it forcefully closes all the resources & services

# mobile  - network, services, display action

# database connection; file resource; network ----> easily hacked


try:
    # file = open("Z:\\status.txt")
    # database = ""
    print(15/10)
except:
    print("you idiot!.....")

finally:  # clause
    # file.close()
    # database.close()
    print("Thanks for your comment....")


# assert ---> single execution to handle error on condition basis
# assert conditon, error_statement(optional)

def aadhaarCardCheck(Card):
    print("valid aadhaar")
    # assert len(Card) > 12, "Not a valid aadhaar"


aadhaarCard = "457954290882"

print(aadhaarCardCheck(aadhaarCard))


x, y = 10, 10
print("value is: ")
assert y != 0, "Should not be zero"  # handling single line execution

'''
Traceback (most recent call last):
  File "c:\Users\pravi\OneDrive\Documents\python-training-082021\day_5\exception_handling.py", line 105, in <module>
    assert y != 0, "Should not be zero"
AssertionError: Should not be zero
'''

print(x/y)
