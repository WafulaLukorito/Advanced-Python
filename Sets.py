#SET is unordered, mutable !Does NOT take duplicates!!!

myset={1, 2, 3, "rice", 3, 1, 2, 2, 3, "rice"} #*Duplicates not printed!!


myset2 = set(["Hello", 1, 5]) #* Another way to declare set, using iterable like list, tuple and string
myset3 = set((2,3,4,5))
myset4=set("Hello world!") #prints individual letters unordered, including space #*notice only one l. Good trick to find how many unique xters in a word.


seta={} #!Empty set recognised as dictionary
setb=set()   #*Proper way to create empty set, using set method

setb.add(4)
setb.add(5)
setb.add(3)
setb.add(6)
setb.add(2)

setb.remove(6) #*raises key error if element not found
setb.discard(6) #* Removes element but if it doesn't find element does not raise key error. 
#setb.clear() #* empties set
#print(setb.pop()) #*returns arbitrary value and removes it

# for i in setb:
#     print(i*i)

# if 1 in setb:
#     print("found it!")
# else:
#     print("hatujapata!")

#----UNION AND INTERSECTION!!----

odds = {1,3,5,7,9}
evens ={2,4,6,8}
primes = {2,3, 5, 7}

#* Union combines stuff from 2 sets without duplication

u = odds.union(evens)

#*Intersection will only take elements in both sets
i = odds.intersection(evens)  #Gives empty set
i2 =odds.intersection(primes)

#---DIFFERENCE OF TWO SETS!!!----

setA= {1, 2,3,4,5,6,7,8,9}
setB= {1,2,3,9,10,11,12, 4}

#* Difference returns a set with all elements from first set not in second set

diff = setA.difference(setB)
diff2=setB.difference(setA)

diff3= setB.symmetric_difference(setA)  #* Returns set with elements in A and B, but not in both

#(setA.update(setB))    #*Updates set A with elements from B

#setA.intersection_update(setB) #*Updates set by keep only elements in both

#setA.difference_update(setB) #*updates A by removing elements found in B 

#setA.symmetric_difference_update(setB) #*Update set with symetric difference with other. 

#--- SUBSET, SUPERSET AND DISJOINT METHODS----

# a= {1,2,3,4,5,6,7,8,9}
# b={1, 2, 3}
# c={22,33}
# print(a.issuperset(b))   #Prints True
# print (b.issubset(a))     #True

#  #*Disjoint return True if both sets have a null intersection (no common elements!!)

# print(a.isdisjoint(b))  #False
# print(a.isdisjoint(c))  #True

#----COPYING SETS---

a= {1,2,3,4,5,6,7,8,9}
b = a  #!Wrong way to copy, if you modify be you modify A since they point to same location

c = a.copy() #*Correct way
d= set(a) #*Another correct way.


#----FROZEN SET!!!--- #*Immutable version of normal set.
a = frozenset([1,2,3,4])

#a.add(2)   #Produces error, immutable!!

print(a)











































































