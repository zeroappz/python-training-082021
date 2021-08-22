def func(listData):
    secondName = [" kumar", " kumar", " kumar",
                  " kumari", " kumari", " kumari"]
    result = list(zip(listData, secondName))
    # return result  # break - flushing the func memory
    # yield result  # it will hold the func memory unless we use the last element
    yield result[0]  # praveen
    yield result[1]  # sriram
    yield result[2]  # deepak
    yield result[3]  # pavithra
    yield result[4]  # priya
    yield result[5]  # sneha


listData = ["praveen", "sriram", "deepak", "pavithra", "priya", "sneha"]
output = func(listData)

# print("yield output: ", next(output))
# print("yield output: ", next(output))
# print("yield output: ", next(output))  # deepak
# print("yield output: ", next(output))
# print("yield output: ", next(output))
# print("yield output: ", next(output))
# print("yield output: ", next(output))   # StopIteration (for loop)


for item in func(listData):
    print('processed Data: ', item)  # handled StopIteration

# acts as a function with yield keyword to hold function memeory until
# reaches the last value like an iterable object
