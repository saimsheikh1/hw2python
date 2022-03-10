def doubler(func):
    def wrapper():
        temp = func()
        return temp * temp
    return wrapper
@doubler
def test():
    print("Hi")

test()