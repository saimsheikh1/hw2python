#Create a file named timeit.py
#Add the following import time to the top of the file
#Create a decorator named calculate_time, decorator is a function that takes another function as its argument and returns another function. ALlow the extension of an original function
#You can use time.time() to get the current time in seconds
#After the decorator computes the time for the function to run it should print EXACTLY 'Total time X' where X is the amount of time it took to run in seconds.
import time
def calculate_time(func):
    def wrapper():
        start = time.time()
        temp = func()       # calling actual fsunction inside wrapper function
        end = time.time()
        timeToRun = end - start
        x = ("Total Time " + str(timeToRun) + " seconds")
        print(x)
        return temp
    return wrapper

@calculate_time
def test():
    i = 10000000
    while i > 0:
        i -= 1
test()

