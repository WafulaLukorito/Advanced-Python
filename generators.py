#* Generators are a simple way of creating iterators. (iter(), next(), StopIteration) are automatically handled by generators in Python. Generators are written like regular functions but use the yield statement whenever they want to return data. Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed). 

#* Generate items inside object lazily, which means that they are generated on the fly (when you ask for them) and not stored in memory. This makes them more memory efficient than lists, especially when dealing with large datasets.

def mygenerator():
    yield 1
    yield 2
    yield 3
    
    
g = mygenerator()
# print (g) # <generator object mygenerator at 0x000001E9F4C5F9D0>

# value = next(g)
# print (value) # 1

# value = next(g)
# print (value) # 2

# value = next(g)
# print (value) # 3

# value = next(g)
# print (value) # StopIteration: no more items to generate

# print (sum(g)) # 6
# sorted(g) #Create and return new list with all objects sorted

# def countdown(num):
#     print('Starting')
#     while num > 0:
#         yield num
#         num -= 1

# cd = countdown(4)

# value = next(cd)
# print (value) # Starting 4

# value = next(cd)  #rememmbers that it was at the point where it yielded 4 and now it will yield 3
# print (value) # 3

# value = next(cd)
# print (value) # 2

def firstn(n):  #function to generate first n numbers. Inefficient, because it creates a list of all numbers in memory before returning it.
    nums = [] #All numbers stored in this list
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

print (firstn(10)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print (sum(firstn(10))) 


def firstn_generator(n): #More efficient, because it generates numbers on the fly and does not store them in memory.
    num = 0
    while num < n:
        yield num
        num += 1

print (sum(firstn_generator(10))) #no need to convert to list, because sum() can take any iterable as input.
import sys

print (sys.getsizeof(firstn(1000000))) # 9000112 bytes
print (sys.getsizeof(firstn_generator(1000000))) # 104 bytes

#* For generators, we don't have to wait until all the items are generated to use them. We can use them one by one. This is called lazy evaluation.

def fibonacci(limit):
    # 0 1 1 2 3 5 8 13...
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b

# fib = fibonacci(30)

# for i in fib:
#     print (i)


#? Generator Expressions
#Written similarly to list expressions

my_generator = (i for i in range(10) if i%2==0 )

for i in my_generator:
    print(i)
    
#You can convert generator item to list with list()
 
my_generator2 = (i for i in range(1000000) if i%2 == 0)
print (sys.getsizeof(my_generator2)) # 208
my_list2 = [i for i in range(1000000) if i%2 == 0]
print (sys.getsizeof(my_list2)) # 4167352