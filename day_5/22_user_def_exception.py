# raise
# raise SyntaxError("Sorry!, it is my fault")

class RegistrationError(Exception):
    pass


raise RegistrationError("Bloddy boy!.....")


'''
Traceback (most recent call last):
  File "c:\Users\pravi\OneDrive\Documents\python-training-082021\day_5\user_def_exception.py", line 8, in <module>
    raise RegistrationError("Bloddy boy!.....")
__main__.RegistrationError: Bloddy boy!.....
'''

'''
Traceback (most recent call last):
  File "c:\Users\pravi\OneDrive\Documents\python-training-082021\day_5\user_def_exception.py", line 2, in <module>
    raise SyntaxError("Sorry!, it is my fault")
SyntaxError: Sorry!, it is my fault
'''

# try, except, finally, raise, assert
