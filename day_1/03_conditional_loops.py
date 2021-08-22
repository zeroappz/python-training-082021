# conditionals: if, if else, if, elif, else
# Looping: while, for, break, continue

import time
if():
    pass
elif():
    pass
elif():
    pass
elif():
    pass
elif():
    pass
elif():  # case
    pass
else:
    pass  # default keyword

# salary - 30000; bank account no - 654321; name - "praveen"
# bankencrypt --> rev(name) + ac ==> "neevarp654321"
# expense: jan - 20%; feb - 18%... dec - 25% ===> (360000-60000) ==> 300000
# Tax %: <= 3L (0%); 8L<= to 3L>= (5%); >=8L (10%)
# encryptedacc, net_amount, tax_amount


# Lift Operation
# 0-10 (0 - GF and 10 - TF) ==> 11 (5 mid position)
# lift is at 5th position
# Praveen is at GF and Sethu is at TF - pressing the button simultaneously
# who will get the priority
# depends on the previous operation - logic behind


# do...while; - exit check - whatsapp - not in python
# while... - entry check - PUBG

'''
do(openApp){
    if(!internet){
        close()
    }
    continue...
}while(internet)

'''

'''
while True:
    # do something
    # on condition meets
    if(!internet):
        break
    else:
        continue
'''
internet = int(input("Internet availblility: "))
# runningMinute = 0
while True:  # infinite
    print("Yes app is loading.....")
    if(internet == 1):
        print("inter is available you can send messages or play games...")
        # runningMinute += 1
        time.sleep(10)  # scheduling
        print("enough playing games.., I am about to close it...")
        break
    else:
        print("No internet!.... closing the app")
        break  # close app on condition fails

else:
    print("statement will execute once while fails")
    print("closing the app......")
# pin = "8643"
# count = 1
# print(id(count))

# while True:
#     pinToCheck = input("Enter your secret PIN...: ")
#     # validation
#     if(pin == pinToCheck):
#         print("navigated to Home page.... ")
#         break
#     else:
#         print("You have entered wrong PIN...")
#         count += 1
#         # print(id(count))
#         if count == 5:
#             print("You have enetered wrong PIN for 5 times...")
#             print("wait for 10 seconds")
#             time.sleep(10)

# windows services ----> always running (while True)
# continue services - internet, database access.....
# network connectivity
