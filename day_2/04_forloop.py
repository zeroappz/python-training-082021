# for each (manual iteration to auto iteration)
# instagram - facebook - whatsapp

# status: message
# message: default message
'''
for (i=0; i<10; i++){
    print(i) # 0, 1,2,3,4,5
    # image, name, time
    # time.sleep(.5)
    for(j=0; j<100; j++){
        print(i) # 0, 1,2,3,4,5
        # image, name, time
        # time.sleep(.5)
    }
}
'''

'''
feed == # image/video, name, desc, time, likes, comment
for (i=0; i==10Billion; i++)
'''
# range(start, stop, step), string, list.....
# TypeError: 'int' object is not iterable
for i in range(10):
    print("value of i is: ", i)

# 3 % 2 ==
# n % 2, %3, %4, %5,%6, %7, %8, %9, % 10 == 1 and n % 11 == 0
# n = int(input("Enter your assumption: "))
for i in range(500, 30000):
    if(i % 2 == 1 and i % 3 == 1 and i % 4 == 1 and i % 5 == 1 and
            i % 6 == 1 and i % 7 == 1 and i % 8 == 1 and i % 9 == 1 and
            i % 10 == 1 and i % 11 == 0):
        print("Net mangoes you have: ", i)
        break
rev = ''
for i in "Praveen":
    rev = i + rev
    print(rev)
