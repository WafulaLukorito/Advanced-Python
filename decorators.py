
import functools
#* There are two types of decorators: function decorators and class decorators.
#* A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it. i.e, it allows you to add new functionality to an existing function/class

#* Function decorators are used to modify the behavior of a function or a method.
#* A function decorator takes a function as an argument, adds some functionality and returns it.
#* Wrappers are used to modify the behavior of a function or a method without explicitly modifying it.

# @mydecorator
# def dosomething():
#     pass

# def start_end_decorator(func):
    
#     def wrapper():
#         print ('start')
#         func()
#         print('end')
#     return wrapper
    

# @start_end_decorator
# def print_name():
#     print("My name is John")
    
# #print_name = start_end_decorator(print_name)

# @start_end_decorator
# def add5(x):
# #     return x+5

# # add5(10)  #!Type Error: wrapper() takes 0 positional arguments but 1 was given

# def start_end_decorator(func):
    
#     def wrapper(*args, **kwargs):
#         print ('start')
#         func(*args, **kwargs)
#         print('end')
#     return wrapper
    

    

# # print_name()

# @start_end_decorator
# def add5(x):
#     return x+5

# add5(10)  #Works now

# result = add5(10) print(result) #!None, because wrapper function does not return anything


# def start_end_decorator(func):
    
#     def wrapper(*args, **kwargs):
#         print ('start')
#         result =func(*args, **kwargs)
#         print('end')
#         return result
#     return wrapper
    

# @start_end_decorator
# def add5(x):
#     return x+5

# result = add5(10)
# print (result) #!15, because wrapper function now returns the result of the original function

# print (help(add5)) #!Shows the wrapper function, not the original function, because the decorator replaces the original function with the wrapper function
# print (add5.__name__) #!wrapper, not add5, because the decorator replaces the original function with the wrapper function
#? To fix, import functools and apply the wrapper to the decorator

import functools

# def start_end_decorator(func):
    
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print ('start')
#         result =func(*args, **kwargs)
#         print('end')
#         return result
#     return wrapper
    

# @start_end_decorator
# def add5(x):
#     return x+5

# print (help(add5))
# print (add5.__name__)

# #? decorator template

# import functools

# def my_decorator(func):
    
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         # Do something before
#         result = func(*args, **kwargs)
#         # Do something after
#         return result
#     return wrapper



# def repeat(num_times):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator_repeat

# @repeat(num_times=3)
# def greet(name):
#     print(f'Hello {name}')
    
# greet('John')

#? nested decorators

# def start_end_decorator(func):

#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print ('start')
#         result =func(*args, **kwargs)
#         print('end')
#         return result
#     return wrapper

# def debug(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
#         signature = ", ".join(args_repr + kwargs_repr)
#         print(f"Calling {func.__name__}({signature})")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__!r} returned {result!r}")
#         return result
#     return wrapper


# @debug
# @start_end_decorator
# def add5(x):
#     return x+5

# result = add5(10)
# print (result)

# @debug
# @start_end_decorator
# def say_hello(name):
#     greeting = f'Hello {name}'
#     print(greeting)
#     return greeting

# say_hello('John')



#* Class decorators are used to modify the behavior of a class. Are typically used when you want to add functionality to a class without modifying the class itself. to modify a state

class CountCalls:
    
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    
    def __call__ (self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print('Hello')
    
say_hello()
say_hello()
say_hello()

#? You can use decorators for stuff like:
# 1. implement timer decorator to measure the time taken by a function to execute
# 2. implement a memoization decorator to cache the results of a function for faster future calls
# 3. implement a logging decorator to log the arguments and return values of a function
# 4. implement a rate limiting decorator to limit the number of times a function can be called
# 5. implement a retry decorator to retry a function if it fails
# 6. implement a authentication decorator to check if a user is authenticated before allowing access to a function
# 7. implement a authorization decorator to check if a user has the correct permissions to access a function
# 8. debug decorator to print the arguments and return values of a function for debugging purposes
