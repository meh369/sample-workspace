
def my_logger(org_fnc):
    import logging 
    logging.basicConfig(filename='{}.log'.format(org_fnc.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return org_fnc(*args, **kwargs)
    
    return wrapper

def my_timer(org_fnc):
    
    import time
    
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = org_fnc(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{org_fnc.__name__} ran in {t2} seconds...')
        return result
    
    return wrapper
    
import time 

@my_logger
# @my_timer
def display_info(name, age):
    print(f'display info ran with args {name}, {age}')

display_info('Mehul', 24)