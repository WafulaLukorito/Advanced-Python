# STRINGS : Ordered, immutable, used for text representation

# my_string = """Hello    #* Tripple quotes used for multiline strings and code documentation
# World!"""

# my_string = """Hello   \
# World!"""               #*Escaping backslash prevents from starting new line

# print(my_string)

stringa = "Hello World!"  # *Access specific character.
char = stringa[-2]
# print(char)
# stringa[3] ='p'  #!Won't work, not mutable!!

substring = stringa[3:]  # *Slicing
substringb = stringa[::-1]  # * Reverse sting!! Cool trick!! Using Step!!

# *Concatenate strings with +

# for i in stringa:
#     i=i.upper()     #* Others: lower(), capitalize(), isupper(), islower(), startswith()
#     print(i)

# print(stringa.startswith("Hello"))

# print(stringa.count("l"))  #*Count how many times a substring appears

# print(stringa.replace("World", "Kenya"))   #*Replace substring with another substring! Returns new string. If substring not found, original string stays the same

# if 'World' in stringa:
#     print ("H imepatikana kuanzia index ")  #  #*Two ways of returning the index of substring, index() and find()
#     print ( stringa.index("W"))
#     print("hadi index")
#     print (stringa.find("d"))
# else:
#     print("Notavailable!!")

stringx = '    Hello  World!    '

# *Removes whitespace before and after string (leading and trailing)
stringx = stringx.strip()

stringx = "".join(stringx.split())  # *Removes ALL whitespaces

# ---LISTS AND STRINGS--- #*Convert string words to lists and vice vers
string_y = "How are you doing "
string_z = "1,2,3,4,5"
list_y = string_y.split()  # *Default delimiter is space.
list_z = string_z.split(",")

# *Convert list to string. Be careful to include delimiter
string_f = ' '.join(list_y)
string_g = ','.join(list_z)


# from timeit import default_timer as timer #*Comparing times!!

# list_orodha = ['a'] * 6000000
# #To join it

# start = timer()
# #!Method 1, long method.
# string_orodha =''
# for i in list_orodha:
#     string_orodha += i    #!Bad Code! Keeps creating new strings, expensive operation!!
# #print(string_orodha)
# stop = timer()
# timetaken=stop-start
# print("The BAD iterative method took " + str(timetaken)+" to complete")


# #*Good Method!! Use join method!!
# startb=timer()
# string_orodha = ''.join(list_orodha) #*Much cleaner and faster!!
# #print(string_orodha)
# stopb=timer()
# timetakenb=stopb-startb

# print("The good join operation took "+ str(timetakenb)+" to complete")

# ---FORMATTING STRINGS---
# * 3 methods: % -old method, .format(), f-String -newest method

var = "TomatoSauce"
var2 = 365
var3 = 3.4155211799
# *Placeholder for string that is filled later with variable
my_string = "the variable is %s" % var
my_string2 = "the variable is %d" % var2  # *Placeholder for number
# * Placeholder for floating point. Rounds to 6 dec places unless specified
my_string3 = "the variable is %.2f" % var3


# ---Format Method---
my_string4 = "the variable is {}".format(var)  # *no need to specify var type!!
my_string4 = "the variable is {:.2f} and {}".format(
    var3, var)  # *Specify 2 dec. plcs and add more variables

# ---f-string method---
my_string5 = f"the variable is {var3}, {var2*26} and {var}"  # * BEST METHOD!!


print(my_string5)
