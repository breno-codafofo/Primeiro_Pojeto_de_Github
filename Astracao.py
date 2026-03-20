def my_decorator(func):
    def wrapper():
        print('Somenthing is happening before the function')
        func ()
        print('Somenthing is happening after the function')
    return wrapper

@my_decorator
def say_whee():
    print('Whee')

say_whee()