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

