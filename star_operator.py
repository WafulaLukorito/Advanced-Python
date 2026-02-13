
#* ASTERISK OPERATOR

# The asterisk operator, also known as the "splat" operator, is used in Python to unpack iterables into individual elements. It can be used in various contexts, such as function arguments, list comprehensions, and more.

#? MULTIPLICATION

print(3 * 4)  # Output: 12

#? POWER

print(3 ** 4)  # Output: 81

#? REPETITION
print("Hello " * 3)  # Output: Hello Hello Hello
zeros = [0] * 5
tuples = [(0, 0)] * 3
print(zeros)  # Output: [0, 0, 0, 0]

#? *args and **kwargs
def sum_all(*args):  #*args allows for variable-length positional arguments
    return sum(args)
print(sum_all(1, 2, 3))  # Output: 6

def print_info(**kwargs):  #**kwargs allows for variable-length keyword arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=30)  # Output: name: Alice, age: 30

#? UNPACKING ARGUMENTS
#* Unpacking arguments allows you to pass a list or dictionary of values as individual arguments to a function. Use * for unpacking lists and ** for unpacking dictionaries.

def add(a, b, c):
    return a + b + c
my_list = [1, 2, 3]
print(add(*my_list))  # Output: 6

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(add(**my_dict))  # Output: 6

#? Why one star for unpacking lists and two stars for unpacking dictionaries?
#* Because lists are ordered, so the elements are unpacked in order, while dictionaries are unordered, so the elements are unpacked by their keys. One star unpacks a sequence (like a list or tuple) into positional arguments, while two stars unpack a mapping (like a dictionary) into keyword arguments.

#? Force keyword arguments
def foo(a, b, *, c, d): #c and d are forced keyword arguments, they must be passed as keyword arguments when calling the function.
    print(a, b, c, d)
foo(1, 2, c=3, d=4)  # Output: 1 2 3 4

#? Unpacking iterables 
#unpacks into a list of individual elements. The number of elements in the iterable must match the number of variables on the left side of the assignment.
my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
print(*my_list)  # Output: 1 2 3
print(*my_tuple)  # Output: 4 5 6

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(*my_dict)  # Output: a b c (unpacking a dictionary with * only unpacks the keys)
print(**my_dict)  # Output: a=1 b=2 c=3 (unpacking a dictionary with ** unpacks the key-value pairs as keyword arguments)

my_list2 = [1, 2, 3, 4, 5,6, 7, 8, 9, 10]
first, *middle, second_last, last = my_list2
print(first)  # Output: 1
print(middle)  # Output: [2, 3, 4, 5, 6, 7, 8]
#print(middle[-1])  # Output: 8 (second last element)
print(second_last)  # Output: 9
print(last)  # Output: 10 

#? MERGE ITERABLES INTO A NEW ITERABLE
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = [*list1, *list2]
print(merged_list)  # Output: [1, 2, 3, 4, 5, 6]

#with tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = (*tuple1, *tuple2)
merged_tuple_list = [*tuple1, *tuple2]
print(merged_tuple_list)  # Output: [1, 2, 3, 4, 5, 6]
print(merged_tuple)  # Output: (1, 2, 3, 4, 5, 6)

#with sets
set1 = {1, 2, 3}
set2 = {4, 5, 6}
merged_set = {*set1, *set2}
print(merged_set)  # Output: {1, 2, 3, 4, 5, 6}

#with dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#? UNPACKING IN FUNCTION DEFINITIONS
def foo(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
foo(1, 2, 3, name="Alice", age=30)

#? UNPACKING IN LIST COMPREHENSIONS
list_of_lists = [[1, 2], [3, 4], [5, 6]]
flattened_list = [item for sublist in list_of_lists for item in sublist]
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]
