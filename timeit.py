import time

# decorator to calculate time to run a function
def calculate_time(func):
    def wrapper():
        start = time.time()    #time right before function starts
        temp = func()
        end = time.time()      #time right after function ends
        runTime = end - start
        x = ("Total time " + str(timeToRun))
        print(x)
        return temp
    return wrapper

@calculate_time
def t1():
    i = 10000000
    while i > 0:
        i -= 1

t1()
