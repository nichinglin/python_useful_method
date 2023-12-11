from functools import wraps
import time

def timer(func):
    @wraps(func)
    def wrapper(a, b):
        start_time = time.time();
        retval = func(a, b)
        print("the function ends in ", time.time()-start_time, "secs")
        return retval
    return wrapper

@timer
def my_func(a, b):
    retval = a+b
    return retval

if __name__ == "__main__":
    my_func(5, 10)