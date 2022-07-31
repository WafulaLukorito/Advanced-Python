

# *Tuples: ordered, immutable, allow duplicate elements

import timeit
import sys
mytuple = ("max", "28", "Boston")  # parenthesis are optional
mytuple1 = ("max")
print(type(mytuple1))  # outputs string
mytuple2 = ("max",)  # single element must be followed coma

mytuple3 = tuple(["kenya", 4, "rwanda"])  # create tuple from a list
print(mytuple3)

item = mytuple[-1]
print(item)

# mytuple[0]="tim" #!Can't work cos tuples are immutable!!

for i in mytuple:
    print(i)

if "tim" in mytuple:
    print("yes")
else:
    print("no00")

print(len(mytuple))

a = ("a", "p", "p", "l", "e")
print(a.count("p"))  # count how many times a letter appears.

print(a.index('p'))  # first occurance of element.


# ** Convert tuple to list
my_list = list(a)
print(my_list)

b = tuple(my_list)
print(b)

# ----SLICING TUPLES---
x = (1, 2, 3, 4, 5, 6, 7, 8, 9)
xa = x[3:6]
xb = x[::-1]  # **reverse a tuple!
xc = x[1::3]
print(x)
print(xa, xb, xc)

# ---UNPACKING TUPLE---
y = "jones", 26, "Nairobi"
name, age, city = y
print(city)
print(name)
print(age)

# my_tuple = (0, 1, 2, 3, 4, 5)

# i1, *i2, i3 = my_tuple

# print(i1)  # 0
# print(i3)  # 5
# print(i2)  # (1, 2, 3, 4)

y_tuple = ("Kenya", "inazidi", "kuenda", "mbele", "pamoja",
           "tushirikiane", "tupendane", "bendera")

i1, i2, *i3, i4 = y_tuple
print(i1)
print(i2)
print(i4)
print(i3)

# ---COMPARE TUPLE AND A LIST--- tuples are better optimized!
test_list = [0, 1, 2, "hello", True]
test_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(test_list), bytes)  # list is larger!
print(sys.getsizeof(test_tuple), bytes)

print("list time")
# list took longer!
print((timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000)))
print("tuple time")
print((timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000)))
