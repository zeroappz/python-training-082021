# dictionary; map(Java), associate array (php)
# hashing, key:value pair

# key must be unique (immutable)        - string, numbers, tuple, frozenset
# value can be duplicates (mutable)     - list, set
# JSON - key:value (API)
dictObj = {
    "mobile": "9047048344",
    "password": "Restricted0",
    "address": ["281, 2nd st", "181, 3rd st", "81, furst st"]
}

# print(dictObj["mobile"])
# print(dictObj["address"][0])

name = ["praveen", "pavithra", "sriram", "jasmine", "arjun"]  # key
values = [
    ["28", "home add", "9047048344", "pravileaf@gmail.com"],
    ["20", "work add", "8797048344", "pravileaf@gmail.com"],
    ["20", "home add", "6747048344", "pravileaf@gmail.com"],
    ["20", "work add", "7747048344", "pravileaf@gmail.com"],
    ["20", "home add", "8947048344", "pravileaf@gmail.com"]
]

dictObj = dict(list(zip(name, values)))
age = dictObj['pavithra'][0]
print('Age of Pavithra is : ', age)
'''
{
    'praveen': ['28', 'home add', '9047048344', 'pravileaf@gmail.com'], 
    'pavithra': ['20', 'work add', '8797048344', 'pravileaf@gmail.com'], 'sriram': ['20', 'home add','pravileaf@gmail.com'], 
    'jasmine': ['20', 'work add', '7747048344', 'pravileaf@gmail.com'], 
    'arjun': ['20', 'home add', '8947048344', 'pravileaf@gmail.com']
}
'''
