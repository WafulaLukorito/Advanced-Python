#Lambda Arguments: Expression
#* A lambda function is a small one line function that is defined without a name.

add10 = lambda x: x+10    #*Will create a function with one argument and return results

#print(add10(99))           #*Calling lambda with an argument.

def add10_funct(x):      #*Similar to lambda, but lambda is much shorter. 
    return x+10

mult =  lambda x, y: x*y     #*Lambda with two arguments

#print (mult(5,9))

#* USe lambda when you need a simple function that is used only once in your code.

#* Can be Used as an argument to higher functions (functions that take in other functions as arguments) example, used alongside built in functions such as sorted(), map(), filter() and reduce().

#SORTED FUNCTION

points2D = [(1,2), (15,1), (5, -1,), (10, 4)]   #*Can think of these of x and y cordinates of points\

points2D_sorted  = sorted(points2D)   #*Sorts list by first argument. #?[(1, 2), (5, -1), (10, 4), (15, 1)]

# print(points2D)
# print (points2D_sorted)    


points2D_sorted2  = sorted(points2D, key= lambda x: x[1])    #*Giving it an argument to sort by second using lambda

#print(points2D_sorted2)   #?  [(5, -1), (15, 1), (1, 2), (10, 4)]

def sort_by_y(x):    #*Performs same function as lambda above. 
    return x[1]



points2D_sorted3= sorted(points2D, key= lambda x: x[0]+x[1]) #*Sorting by sum of x and y.

#print(points2D_sorted3)


#------MAP FUNCTIONS----

#*Map functions transform each element with a function.
#* map (func, seq)

a= [1,2,3,4,5]
b = map(lambda x: x*2, a)

#print(list(b))    #!Must convert map object to list!

c = [x*2 for x in a]    #*Achieving the same with list comprehension. Many ways to kill a rat!!
#print (c)

#-----FILTER FUNCTION!!!----
#*filter (func, seq)
#*Returns true or false
#*Filter function returns all elementsfor which the function evaluates to true. 

a1=[1,2,3,4,5,6]
b1= filter(lambda x: x%2 != 0, a1)
#print(list(b1))

c1= [x for x in a1 if x%2 !=0]   #*Can achieve same thing with list comprehension
#print (c1)

#----REDUCE FUNCTION!!!---
#*Also takes function and sequence. Repeatedly applies function to elements and returns a single value. 
from functools import reduce  #*Must import!!

a2 = [1,2,3,4]
prod_a2 = reduce(lambda x, y : x*y, a2)   #*Finding product of Elements. Reduce function always has two argumenents. #?24
print (prod_a2)


























