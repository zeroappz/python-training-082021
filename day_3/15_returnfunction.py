import time


def short_hand():
    ''' this is to check performance using short hand operator '''
    listData = []
    start = time.time()  # nano seconds
    for i in range(100000):  # 0, 9
        listData += [i]  # 3 steps
    end = time.time()  # nano secondsclearclear
    print("Shorthand Time Taken: ", end-start)


def append_fun():
    ''' this is to check performance using append() '''
    listData = []
    start = time.time()  # nano seconds
    for i in range(100000):
        listData.append(i)
    end = time.time()  # nano seconds
    print("Time Taken for append(): ", end-start)


def normal_operator():
    '''This is to check performance using normal operator '''
    listData = []
    start = time.time()  # nano seconds
    for i in range(100000):  # 0, 9
        listData = listData + [i]
    end = time.time()  # nano seconds
    print("Normal Operator Time Taken: ", end-start)


def send():
    short_hand()
    append_fun()
    # normal_operator()


def documentation():
    print(short_hand.__doc__)
    print(append_fun.__doc__)
    print(normal_operator.__doc__)


def main():
    send()
    documentation()


main()  # supermost function
