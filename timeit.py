import time

# decorator to calculate time to run a function
def calculate_time(func):
    def wrapper():
        time_start = time.time()    
        temp = func()               #calling actual function inside wrapper function
        time_end = time.time()      
        timeToRun = time_end - time_start
        string = ("Total time " + str(timeToRun))
        print(string)
        return temp
    return wrapper

@calculate_time
def test():
    i = 10000000
    while i > 0:
        i -= 1

test()
