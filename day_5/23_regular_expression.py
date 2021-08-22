# key role on validations
# strings validation -----> string validation

# registration form
'''
Forms:
    1. name
    2. mobile
    3. email
    4. password
    5. true or false
    ---->submit

URL: 
    1. Ipaddress
    2. url

number = input()
pattern = ""
'''

'''
    1. Character Class
    2. Quantifiers
    3. MetaCharacter Class

Character Class:

    1) .        - it compares any charcter (alpha, num & special charcters)
    2) [0-9][0-9][0-9]    - it matches a number from 0 to 9; 000 --- 999 
    3) [a-z][m-x]    - comapre alphabets lower case
    4) [0-9|a-f][0-9|a-f][0-9|a-f][0-9|a-f]       - 0000 ---> ffff (0-9 or a-f 4 characters)
    5) [#$@!]
    6) [A-Z]    - upper case
    7) [], (), {}
    8) | - either or
    9) ^, $
    10) ? - optional

Quantifiers:
    1. {n}  - n number of times; {10}
    2. {n, m}  - n number of times; {8, 16}
    3. {n, }   - {8, } -----> minimum 8 charc and max n length

Metacharacters:
    1) \d ----> [0-9]; 
    2) \D ----> "^[a-zA-Z#$%@!]$"
    3) \w ----> "[a-zA-Z]"
    4) \W ----> "[0-9#$%#@!]"
    5) \s ----> 
    6) \S ----> exlusive of spaces
    7) +  ----> minimum 1 occurences to max n ---> {1, }
    8) *  ----> minimum 0 occurences to max n ---> {0, } - print()
    print(*args), print(a, b, c, d, e)
'''

import re # regular express
pattern = "[0-9|a-f]{4}"         # - hexadecimal

mobile_pattern = "^[6789][0-9]{9}$"       # 0000000000; 9999999999 - 6789
mobile_pattern = "^[6789]\d{9}$"

pattern_bsnl = "94437[0-9]{5}"

# re.search()     # search(pattern, string)
statement = "India*is*mycountry*India*is good and India is bad at some"

output = re.search("India$", statement)
print(output)
# <re.Match object; span=(0, 5), match='India'>
# <re.Match object; span=(20, 25), match='India'>

result = re.findall("India", statement)
print(result)           # list of data

result = re.split("\*", statement)
print(result)

dob = "26-11-1992"
result = re.split("-", dob)
print(result)       # ['26', '11', '1992'], d-m-y; y-m-d
print("day {} month {} and year {}".format(result[0], result[1], result[2]))


# split(), findall(), search(), match(),


# Password must have 8 characters minimum and 16 as max with special characters
# support of #$%@
password = "^[a-zA-Z0-9#%@]{8, 16}$"

# Restricted@0
# abcd@1234

# ipaddress ----> 0.0.0.0 to 255.255.255.255
# ipaddress = "[0-9]{3}"          # 0, 111, 999
'''
step 1: 250 to 255
step 2: 200 to 249
# step 3: 100 to 199
step 4: 0 to 199
'''

ipaddress = "^25[0-5]|2[0-4][0-9]|[0-9]?[0-9]?[0-9]\.{3} (25[0-5] | 2[0-4][0-9] | [0-9]?[0-9]?[0-9]$"

# input = 0
# input = 19
# input = 199
# [0-255] = single data
# 255.255.255.
# 255.255.255.255
# 0.0.0.0
# 192.168.1.10
# -- validate ipaddress

# landline --> "^[2-5][0-9]{7}$"
# name ------> "^[a-zA-Z0-9_\.]+$"

# ipv4 and ipv6 ----> win+r ==> ipconfig
'''
IPv6 Address. . . . . . . . . . .: 2405: 201: e01c: 70e0: 59be: a7e3: ba49: f6fa
Temporary IPv6 Address. . . . . .: 2405: 201: e01c: 70e0: d89a: 900a: d42c: 97f4
Link-local IPv6 Address . . . . .: fe80:: 59be: a7e3: ba49: f6fa%12
IPv4 Address. . . . . . . . . . .: 192.168.29.9
'''

ipv6 = "^([0-9a-f]{4}\: )([0-9a-f]{3}\: )([0-9a-f]{4}\: ){6}$"
