# COLLECTIONS: Counter, namedtuple, OrderedDict, defaultdict, deque
# * Implements special container datatypes and provides alternatives with some additional functionality
# * compared to general containers like dictionaroes, lists or tuples.

# ----COUNTER----
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import OrderedDict, namedtuple
from collections import Counter  # *Don't forget to import!!

# *Counter stores elements as dictionary keys and their counts(how often they appear) as dictionary values

a = "aaaaaabbbbbcccc"
# ?Will be Counter({6: 2, 0: 2, 1: 2, 2: 1, 4: 1, 7: 1})
b = [6, 0, 2, 1, 4, 7, 0, 1, 6]
my_counter = Counter(a)
# print(my_counter)  #?Prints Counter({'a': 6, 'b': 5, 'c': 4})

# *Since it's a dictionary we can do normal dict functions
# print(my_counter.items())  #?Prints dict_items([('a', 6), ('b', 5), ('c', 4)])
# print(my_counter.values()) #?Prints dict_values([6, 5, 4])
# print(my_counter.keys())  #?dict_keys(['a', 'b', 'c'])

#  for value in my_counter.values():
#      print (value*100)

# print (my_counter.most_common(1)[0[0]]) #?Prints a
# print (my_counter.most_common(2))    #*View most common item(s). Returns list with tuples inside. #?Will print [('a', 6), ('b', 5)]. The indicates we want top 2 items
# print (my_counter.most_common(2)[1])  #? Prints second most common item, ('b', 5)
# print (my_counter.most_common(2)[1][0]) #?Prints b

# print (list(my_counter.elements()))  #*Iterator over elements repeating each as many times as its count.


# -----NAMED TUPLES-----

# Point = namedtuple('Point', 'x, y')  #*Will create class Point with fields x and y
# pt = Point(1,-4)
# print (pt)
# print (pt.x, pt.y)

# #* Python code to demonstrate namedtuple()


# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)

# #*Another named Tuple example
# Point2 = namedtuple('Point', 'x y')
# pt1 = Point2(1.0, 5.0)
# pt2 = Point2(2.5, 1.5)

# from math import sqrt
# line_length = sqrt((pt1.x-pt2.x)**2 + (pt1.y-pt2.y)**2)

# print (line_length)


# ----OrderedDict----
# * Just like ordinary dictionary, but it remembers order in which items were inserted
# * Become less important since common dictionary class was given ability to remember

# ordered_dict =OrderedDict()

# ordered_dict['b'] = 2
# ordered_dict['c'] = 3
# ordered_dict['d'] = 4
# ordered_dict['a'] = 1

# normal_dict ={}   #*Normal dict also remembers

# normal_dict['b'] = 2
# normal_dict['c'] = 3
# normal_dict['d'] = 4
# normal_dict['a'] = 1
# #print(normal_dict)


# #----DEFAULT DICT----
# #* Similar to ordinary dict but has default value if key is not set yet


d = defaultdict(int)  # *Default type int
d['a'] = 1
d['b'] = 2

# print(d)  # ? prints defaultdict(<class 'int'>, {'a': 1, 'b': 2})
# print(d['a'])  # *Access the key a
# print(d['b'])  # *Access key b
# # *When not assigned, prints default int value, 0. #!Raises key error with normal dictionary. #Creates new key with default value of int 0.
# print(d['c'])
# print(d)  # ? defaultdict( < class 'int' > , {'a': 1, 'b': 2, 'c': 0})


# e= defaultdict(float)    #*Default type float
# e['a'] = 5
# e['b'] =  6
# print(e)
# print (e['a']) #*Access the key a
# print (e['b'])  #*Access key b
# print (e['c']) #*When not assigned, prints default float value, 0.0
# print (e['d'])


# f= defaultdict(list)    #*Default type empty list or tuple #!Raises key error with normal dictionary.
# f['a'] = 5
# f['b'] =  6
# print(f)
# print (f['a']) #*Access the key a
# print (f['b'])  #*Access key b
# print (f['c']) #*When not assigned, prints default list or tuple value, empty
# print (f['d'])


# -----DEQUE-------
# * A double-ended queue, can be used to add or remove elements from both ends.
# * Implemented in a very efficient manner.

my_deque = deque()
my_deque.append(1)  # *Normal append like list, to the right side
my_deque.append("Loo si far")
my_deque.append(99)

# *Adds elements at the left side of deque
my_deque.appendleft({'mji': 'Nairobi'})
my_deque.appendleft((3, 9))
#print (my_deque)
my_deque.pop()  # *Normal remove of elements to the right
my_deque.popleft()  # *Remove items from left
#print (my_deque)

# *Can extend deque with multiple elements at a time using list. "Kaswende" will be most left element
my_deque.extend([4, 5, 6, "kaswende"])
# *Extends to the left. *// Note! -34 is added the leftest!!!
my_deque.extendleft([32, "Rwanda", -34])

print(my_deque)


my_deque = deque()

my_deque.extend([1, 2, 3, 4, 5])

# *Rotates elements one place to the right! Basically puts last element first.
# my_deque.rotate(1)
# print(my_deque)  # *[5, 1, 2, 3, 4]
# *Rotates elements two places to the right
# my_deque.rotate(2)
# print(my_deque)  # *[4, 5, 1, 2, 3]
# # *Rotates on place to the left! Basically puts second element first!
my_deque.rotate(-1)
print(my_deque)  # *[2, 3, 4, 5, 1]

# for item in my_deque:  #*Iterate over deque
#     if type(item)==int:
#         print (item*1000)
#     else:
#         print (item)

# my_deque.clear() #*Remove all elements, returns empty deque.
# print (my_deque)
