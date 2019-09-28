def decorator(func):
    def wrapper(*args, **kwargs):
        print("I'm before the function call!")
        func(*args, **kwargs)
        print("I'm after the function call!")
    return wrapper


@decorator
def func(*args):
    result = 0
    for i in args:
        result += i
    print("Sum = ", result)


func(1, 3, 45, 77)
