def decorator_function(orignal_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper fn executed before {orignal_function.__name__}')
        return orignal_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print('display fn running..')

### for class 

class Decorator_class(object):
    
    def __init__(self, orignal_function):
        self.orignal_function = orignal_function

    def __call__(self, *args, **kwargs):
        print(f'call method executed before {self.orignal_function.__name__}')
        return self.orignal_function(*args, **kwargs)


@decorator_function()
def display():
    print('display fn running..')



@decorator_function
def display_info(name, age):
    print(f'display info ran with args {name}, {age}')

display_info('Mehul', 24)
display()   