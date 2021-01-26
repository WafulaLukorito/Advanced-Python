# ITERTOOLS: product, permutations, combinations, accumulate, group by and infinite iterators
#* A collection of tools for handling iterators. Iterators are data types that can be used in a for-loop
#* Used for efficient looping 

#----PRODUCT----

from itertools import product

a = [1,2]
b = [3, 4]
c=[3]
prod = product (a, b) #*Will compute cartesian product

#print (list(prod))   #*Convert it to list to see the elements

prod2 = product (a, b, repeat=2)   #*Can also define number of repetitions
prod3 = product (a, c, repeat=2)
#print (list(prod3))  

#---PERMUTATIONS----
#*Permutations will return all possible orderings of an input
from itertools import permutations

a1= [1,2,3]
perm = permutations(a1)
#print (list(perm))   #*Convert to list before printing!!

perm2= permutations(a1 , 2) #*Can specify length of permutations!!
#print (list(perm2))

#----COMBINATIONS!----
#* Will make all possible combinations with a specified length.
from itertools import combinations  #*No repetitions!!
a2= [1, 2, 3, 4]
a21 = ["b", "a", "n", "a", "n", "a"]
comb = combinations(a21, 3)  #*Second argument is mandatory!
#print (list(comb))

from itertools import combinations_with_replacement  #*Allows repetitions!!
a22 = [1, 2, 3, 4]
combrep= combinations_with_replacement(a22, 4)
#print(list(combrep))

#----ACCUMULATE!----
#*Makes an iterator that returns accumulated sums or any other binary functions that are given as input
from itertools import accumulate
a3 = [1, 2, 3, 4]
acc = accumulate(a3)   #*Computes sums by default
#print (a3)
#print(list(acc))    #*Prints Cumulative values!!

import operator #*Other functions
acc2 = accumulate (a3, func=operator.mul)   #*Multiples cumulatively!
#print(list(acc2))

a31=[1,2,5,4, 3, 1, 0]
acc3 = accumulate (a31, func=max)   #*Returns max for each comparison
#print(list(acc3))


#----GROUP BY----
# #* Makes an iterator that returns keys and groups from an iterable
from itertools import groupby

# def smaller_than_3(x):
#     return x < 3

# a4= [1,2,3,4, 5,6,7,8,9]
# group_obj = groupby(a4, key=smaller_than_3) #*Assign function as key

# for key, value  in group_obj:     #*Iterate over group_obj
#      #print (key, value)         #* values still in itertools form. 
#      #print (key, list(value))



# def is_even(x):
#     y= x%2
#     return y>0

# for 
# a41= [1,2,3,4, 5,6,7,8,9]

# group_obj2 = groupby(a41,key=is_even)

# for key, value in group_obj2:
#     print (key,list(value))



#*Can be done using lambas  (small one line functions that can return an input.)

def smaller_than_3(x):
    return x < 3

a4= [1,2,3,4, 5,6,7,8,9]
group_obj = groupby(a4, key=lambda x: (x <3)) #*Assign key with Lambda!!

# for key, value  in group_obj:     #*Iterate over group_obj
#      #print (key, value)         #* values still in itertools form. 
#      print (key, list(value))

persons = [{'name': 'Tim', 'age' : 25 }, {'name': 'Dan', 'age' : 25 }, {'name': 'Lisa', 'age' : 27 }, {'name': 'Claire', 'age' : 28 }]

group_obj3 = groupby(persons, key=lambda x : x ['age'])
# for key, value in group_obj3:
#     print (key, list(value))


#----INFINITE ITERATORS!!!----
from itertools import count, cycle, repeat

#----COUNT FUNCTION!!---
# for i in count(10):   #* Counts from ten, adding one, till infinity. 
# #     print(i)         #!Very dangerous!! Infinite loop! Put break case!!
# for i in count (10):
#     print(i)
#     if i==15:
#         break


#---CYCLE!!---
#*Will cycle infinitely through a list!
cyclist= [1,2,3]

# for i in cycle(cyclist): #*Will just cycle, don't try this at home!
#     print (i)


#----REPEAT!!!



# for i in repeat(1):
#     print (i)      #*Will print 1 until Jesus Comes
import time
for i in repeat("Jesus", 30): #*Will print "Jesus" 30 times, after every 5 seconds.
    time.sleep(5)
    print (i)