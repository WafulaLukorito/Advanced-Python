
#* There are two types of decorators: function decorators and class decorators.
#* A decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.

#* Function decorators are used to modify the behavior of a function or a method.
#* A function decorator takes a function as an argument, adds some functionality and returns it.
#* Wrappers are used to modify the behavior of a function or a method without explicitly modifying it.

# @mydecorator
# def dosomething():
#     pass


def print_name():
    print("My name is John")

#* Class decorators are used to modify the behavior of a class.