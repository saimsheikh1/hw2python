# decorator to track number of times a function is called
def func_counter(func):
    def wrapper(*args, **kwargs):       #accept an arbitrary number of positional and keyword arg
        wrapper.counter += 1  # when function called add 1 to counter
        return func(*args, **kwargs)        
   # reset wrapper counter
    wrapper.counter = 0
    # return new decorated function
    return wrapper

# test the func_counter()
@func_counter
def hello():
    print("hello")


x = 0
while (x < 5):
    hello()
    x += 1


helloCount = hello.counter
print(helloCount)    