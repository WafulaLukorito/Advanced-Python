#* Dictionaires: key-value pairs, Unordered, Mutable

mydict = {"name": "Wafula", "age": 26, "city": "Nairobi"}

print (mydict)

mydict2= dict (jina="Jones", umri=23, jiji = "Ruiru", kiambo="Kairu")

value=mydict2["jina"]


mydict2["anwani"]="332, Ruiru" #* insering stuff inside


mydict2["anwani"]="444, Kimbo"  #*will get overwritten

del mydict2["jiji"]


mydict2.pop("kiambo") #* another way to delete

mydict2.popitem() #* Removes last inserted item

# if "name3" in mydict:  #*Check if item is on the list
#     print (mydict["age"])
# else:
#         print("hakuna!")

# try:                             #*Checking if item is in by throwing exception
#     print(mydict["name2"])
# except:
#     print("ugali beans, not found!")

# for key in mydict:     #Works the same as for key in mydict.keys()
#  print(key)

# for value in mydict.values():   #* Iterating over values
#  print(value)
item2=mydict.keys()
item=mydict.values()  #*Returns list will all values in it

# for key, value in mydict.items(): #* iterate over both keys and values
#     print (key,value)

mydict_cpy=mydict    #! Copying list. Wrong way! If we modify copy we modify original too as they point to same location!!

mydict_copy= mydict.copy()   #*Proper way to copy dict. Original won't change if we modify copy.

mydict_copy2= dict(mydict)   #*Another way to properly copy. 

#Merge two dictionaries, update method!
a={"name": "Wafula", "age": 26, "city": "Nairobi", "email": "abc@xyz.com", "job": "Thief"}
b={"name": "Nasike", "age": 18, "city":"Bungoma"}

a.update(b)

#print (a)

#* You can aslo use tuples as keys
mytuplea=(8,7)
mydicta= {mytuplea:54} #? {(8, 7): 54}

print (mydicta)

#*Cannot use lists as keys!! Lists are not hashable
mylista=[2,3]
#mydictb={mylista:3}
#print(mydictb) # !Doesn't Run!!!
























