'''
- The difference between arguments and parameters 
- The different types of arguments (positional, keyword, default, variable-length)
- Container unpacking (using * and ** to unpack lists and dictionaries into function arguments)
- local vs global variables (scope of variables within functions)
- parameter passing (by object reference)

'''

#* Arguments are the actual values passed to a function when it is called, while parameters are the variables defined in the function's signature that receive those values.

# def my_function(param1, param2):  #param1 and param2 are parameters
#     return param1 + param2

# result = my_function(5, 10)  #5 and 10 are arguments
# print(result)  # Output: 15


#? Positional arguments are passed to a function in the order they are defined, while keyword arguments are passed using the parameter names, allowing for more flexibility in the order of arguments.

def  greet(name, greeting="Hello"):  #greeting is a default argument
    return f"{greeting}, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
print(greet("Bob", greeting="Hi"))  # Output: Hi, Bob!

#keyword arguments can be used to specify arguments in any order, while positional arguments must be passed in the correct order.

def display_info(name, age):
    return f"Name: {name}, Age: {age}"

print(display_info("Alice", 30))  # Output: Name: Alice, Age: 30
print(display_info(age=30, name="Alice"))  # Output: Name: Alice, Age: 30

#? Combine positional and keyword arguments in a function call, but positional arguments must come before keyword arguments.

def introduce(name, age, city="Unknown"):
    return f"My name is {name}, I am {age} years old, and I live in {city}."

print(introduce("Alice", 30))  # Output: My name is Alice, I am 30 years old, and I live in Unknown.
print(introduce("Bob", 25, city="New York"))  # Output: My name is Bob, I am 25 years old, and I live in New York.

#? Combine positional and keyword arguments and default arguments in a function definition, but positional arguments must come before keyword arguments, and default arguments must come after all non-default arguments.

def create_user(username, password, email=None):
    return f"Username: {username}, Password: {password}, Email: {email}"

print(create_user("user1", "pass123"))  # Output: Username: user1, Password: pass123, Email: None
print(create_user("user2", "pass456", email="user2@example.com"))  # Output: Username: user2, Password: pass456, Email: user2@example.com 

#* Variable-length arguments allow a function to accept an arbitrary number of positional or keyword arguments. Use *args for variable-length positional arguments and **kwargs for variable-length keyword arguments.

def sum_all(*args):  #*args allows for variable-length positional arguments
    return sum(args)
print(sum_all(1, 2, 3))  # Output: 6

def print_info(**kwargs):  #**kwargs allows for variable-length keyword arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=30)  # Output: name: Alice, age: 30

# *args and **kwargs can be used together in a function definition, but *args must come before **kwargs.

def mixed_arguments(arg1, *args, kwarg1=None, **kwargs):
    print(f"arg1: {arg1}")
    print(f"args: {args}")
    print(f"kwarg1: {kwarg1}")
    print(f"kwargs: {kwargs}")
mixed_arguments(1, 2, 3, kwarg1="Hello", key1="Value1", key2="Value2")  # Output: arg1: 1 args: (2, 3) kwarg1: Hello kwargs: {'key1': 'Value1', 'key2': 'Value2'} 


#* Forced keyword arguments can be used to require certain arguments to be passed as keyword arguments, even if they are defined as positional parameters in the function signature. This is done by placing a * in the function definition before the parameters that should be forced as keyword arguments.

def forced_keyword_arguments(arg1, *, kwarg1, kwarg2):
    print(f"arg1: {arg1}")
    print(f"kwarg1: {kwarg1}")
    print(f"kwarg2: {kwarg2}")
forced_keyword_arguments(1, kwarg1="Hello", kwarg2="World")  # Output: arg1: 1 kwarg1: Hello kwarg2: World  

def foo(a, b, *, c, d): #c and d are forced keyword arguments, they must be passed as keyword arguments when calling the function.
    print(a, b, c, d)
foo(1, 2, c=3, d=4)  # Output: 1 2 3 4

def foo2(*args, c, d): #c and d are forced keyword arguments, they must be passed as keyword arguments when calling the function.
    print(args, c, d)
foo2(1, 2, c=3, d=4)  # Output: (1, 2) 3 4

def foo3(*args, last_arg): #last_arg is a forced keyword argument, it must be passed as a keyword argument when calling the function.
    print(args, last_arg)
foo3(1, 2, 3, last_arg=4)  # Output: (1, 2, 3) 4



#? UNPACKING ARGUMENTS
#* Unpacking arguments allows you to pass a list or dictionary of values as individual arguments to a function. Use * for unpacking lists and ** for unpacking dictionaries.

def add(a, b, c):
    return a + b + c
my_list = [1, 2, 3]
print(add(*my_list))  # Output: 6

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(add(**my_dict))  # Output: 6

#? Why one star for unpacking lists and two stars for unpacking dictionaries?
#* Because lists are ordered, so the elements are unpacked in order, while dictionaries are unordered, so the elements are unpacked by their keys. Onne star unpacks a sequence (like a list or tuple) into positional arguments, while two stars unpack a mapping (like a dictionary) into keyword arguments.

# #* says: “Take this iterable and spread its values into positional arguments.”
# • 	 says: “Take this mapping and spread its key–value pairs into keyword arguments.”
# • 	Lists/tuples don’t have named keys, so they can only be unpacked positionally. Dicts do have keys, so they can be unpacked as named arguments.

#* in unpacking, the number of elements in the list or dictionary must match the number of parameters in the function definition. If there are too many or too few elements, a TypeError will be raised.


#? LOCAL vs GLOBAL ARGUMENTS
#* Local variables are defined within a function and can only be accessed within that function, while global variables are defined outside of any function and can be accessed from anywhere in the code.

x = 10  # global variable

def my_function():
    x = 5  # local variable
    print(x)  # Output: 5

def another_function():
    global number  # This allows us to modify the global variable 'number' inside this function
    number = 20  # This modifies the global variable 'number'
    print(number)  # Output: 20

my_function()  # Output: 5
print(x)  # Output: 10
another_function()  # Output: 20 
print(number)  # Output: 20 (the global variable 'number' has been modified by another_function)

def foo():
    global num
    y = num
    num = 3
    print ('number inside function:', y) 
foo()  # Output: number inside function: 3
num = 5
print ('number outside function:', num)  # Output: number outside function: 5

#? Parameter Passing (by object reference)
#* In Python, arguments are passed to functions by object reference. This means that when you pass a mutable object (like a list or dictionary) to a function, any changes made to that object within the function will affect the original object outside the function. However, if you pass an immutable object (like an integer or string), any changes made to that object within the function will not affect the original object outside the function.

def modify_list(my_list):
    my_list.append(4)  # Modifies the original list
my_list = [1, 2, 3]
modify_list(my_list) 
print(my_list)  # Output: [1, 2, 3, 4]

def modify_integer(my_int):
    my_int += 5  # Does not modify the original integer
    return my_int  # Return the modified value instead of modifying the original

original_int = 10
new_int = modify_integer(original_int)
print(original_int)  # Output: 10 (unchanged)
print(new_int)       # Output: 15 (new value returned by the function)

#* Instances where a mutable (list, etc) has a local variable can be confusing 
def test_function(my_list):
    my_list = [1, 2, 3, 4] # This creates a new local list object, it doesn't modify the original list
    print(my_list)  # Output: [1, 2, 3, 4]


