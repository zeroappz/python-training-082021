# dictionary - indulge (key ---> values)
# key - unique
# values - anything or any number
# Hashing technique
# random - best case / worst case (algorithm)


'''
reach destination 
- Chennai to Delhi

- Mode of Transportation
        (Mode)          (Best - Time)          (Worst - Money)
    1) Airlines         Best                    Worst
    2) Train            
    3) Car              
    4) Bus
    5) Bike 
    6) Cycle            Worst                  Best

- Linear DS (Array) - 30 members
    Search: 1st (best)  -----> 30th (worst) --- ('Praveen')

- Non-Linear (Tree; Graph)
    Search: male (15) & female (15) ----->  ('Praveen' - 'Male')
'''

obj = dict()
obj = {}  # set = set()
# print(type(obj))
# {key: value(s)}

register_form_tile = ["fname", "lname",
                      "email", "password", "address", "mobile"]
# fname = input('Enter your name: ')

reg_form_value = ["Sneha", "Prasanna",
                  "sneha2021@gmail.com", "Restricted", [
                      "home address", "work address"],
                  "9047048344"]

userData = dict(list(zip(register_form_tile, reg_form_value)))
print(userData)

# access values using key
print('Welcome Ms.', userData['fname']+userData['lname'])
print('Product has been delivered to the address: ', userData['address'][0])

# print(userData['age'])      # KeyError: 'age'
print(userData.get('mobile'))    # None

# looping
print('\nDict keys are: ', userData.keys())

if userData.get('age') == None:
    userData['age'] = 25
    print('dict Value: ', userData)
else:
    print('Age already available...')

for key, value in userData.items():
    print('key: ', key)
    print('value: ', value)

for key in userData.keys():
    print('key: ', key)

for value in userData.values():
    print('Value: ', value)

# update(obj)
userData['dept'] = 'CSE'
userData.update({'skills': ['Programming', 'Fluency']})
print()
print(userData)

'''
{
    'fname': 'Sneha', 
    'lname': 'Prasanna', 
    'email': 'sneha2021@gmail.com', 
    'password': 'Restricted', 
    'address': ['home address', 'work address'], 
    'mobile': '9047048344', 
    'age': 25, 
    'dept': 'CSE', 
    'skills': ['Programming', 'Fluency']
}

'''

# pop(), items(), keys(), values, update(), clear(), zip()
# del userData['age']
# del userData


'''
Hospital Management System
    1) Employees List - (doctor, nurses)
    2) Rooms & Beds Availability -  charge
    3) Patient presence - Dynamic
    4) Patient map - doctor, nurse, room, bed, days, charges

    5) Fetching Data: patientname - where he is?, ....
    6) discharge - room charge (days)
'''
