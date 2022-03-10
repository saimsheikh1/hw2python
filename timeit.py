#Create a file named timeit.py
#Add the following import time to the top of the file
#Create a decorator named calculate_time, decorator is a function that takes another function as its argument and returns another function. ALlow the extension of an original function
#You can use time.time() to get the current time in seconds
#After the decorator computes the time for the function to run it should print EXACTLY 'Total time X' where X is the amount of time it took to run in seconds.
import time
def calculate_time(func):
    def wrapper():
        start = time.time()
        func()       # calling actual fsunction inside wrapper function
        end = time.time()
        runTime = end - start
        output = ("Program run time " + str(runTime))
        print(output)
    return wrapper

@calculate_time
def t1():
    i = 10000000
    while i > 0:
        i -= 1
t1()

