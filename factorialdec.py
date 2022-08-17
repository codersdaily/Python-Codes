'''
*args and **kwargs are special keyword which allows function to take variable length argument.

*args passes variable number of non-keyworded arguments and on which operation of the tuple can be performed.
**kwargs passes variable number of keyworded argument on which operation of dictionary can be performed.

The functools module, part of Python’s standard Library, provides useful features that make it easier to work with high order functions (a function that returns a function or takes another function as an argument ). With these features, you can reuse or extend the utility of your functions or callable object without rewriting them. This makes the writing of reusable and maintainable code to be quite simple.

wraps()
It is a convenience function for invoking update_wrapper() to the decorated function. 
It is equivalent to running partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated).
'''



from functools import wraps
from time import time
def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            print(f"Total execution time: {end_ if end_ > 0 else 0} ms")
    return _time_it

@measure
def hello():
    print('hello world')

hello()