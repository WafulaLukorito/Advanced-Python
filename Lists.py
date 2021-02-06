# Lists:ordered, mutable, allows duplicate elements
mylist = ["banana", "cherry", "apple", "wafula"]
print(mylist)

#*Find index of element in list

#index= mylist.index(element)

# mylist2=[5, True, "apple", "apple"]
# print(mylist2)

# for i in mylist:
#     print(i)

# if "wafula3" in mylist:
#     print("wafulastock")
# else:
#         print("noooo")

#         print (len(mylist))
# mylist.append("alufaw")
# print(mylist)

# mylist.insert(-1, "ugalibeans")
# print(mylist)

# (mylist.pop(0))
# print (mylist)

# mylist.remove("apples")
# print(mylist)

# item=mylist.clear()
# print(mylist)

item=mylist.reverse()
print(mylist)


# # # mylist.sort()
# # # print(mylist)

# # new_list = sorted(mylist)
# # print(new_list)


# # mylist3=["rice"]*5
# # print(mylist3)

# # mylist4=[1,2,3,4,5]
# # mylist5=mylist3 + mylist4
# # print(mylist5)



# newlist= [1, 2, 3,4,5,6,7,8,9]

# a=newlist[1:6] #slicing
# print (a)

# b= newlist[3:]
# c=newlist[:7]
# print(a, b, c)

# d=newlist[::3]  #step
# print (d)

# e=newlist[::-1] #reverse list with negative step
# print(e)

# list_org =["banana", "cherry", "apple"] #Copying
# list_cpy =list_org #With this, if you modify the copy, you also modify the original.
# #list_cpy.append("lemon")
# #print(list_org)   #both lists refer to the same object inside memory!!!

# list_cpy= list_org.copy()  #proper copying method!!
# print(list_org)

# #--- list function copying---- another method to make actual copy
# list_cpy2 = list(list_org)

# #---Copying with slicing!
# list_cpy3 = list_org[:]   #Slices from begining to end, making actual copy.

#-------LIST COMPREHENSION--- fast way to create new list from existing list
numlist=[1, 2, 3, 4, 5, 6]
numlist2= [i*i for i in numlist] #**easy way to generate squares 
# print (numlist, numlist2)









































