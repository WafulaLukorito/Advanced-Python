# EXCEPTIONS AND ERRORS: Python Program terminate as soon as they encounter syntax or exception errors.

# ----SYNTAX ERROR---
# *Occurs when parser detects syntactically incorrect statement

# a = 5 print (a)  #!Syntax error.
# print (a))   #! Syntax error.

# ----EXCEPTIONS----
# *Statement is syntactically correct bu causes an error when executed.

# *Type error --e.g, trying to add number to a string.
#a = 5 + '10'

# import somemodulethatdoesnotexist  #*Raises module not found error.

# a = c   #*NameError, name C not defined

# f = open('someNonexistenFile.txt')  #*File not found error!

# *ValueError, when function or expression receives statement of right type but inappropriate value.
# a = [1,2,3]
# a.remove[4]  #!Value error!
# *IndexError, Occurs when you want to access non-existent index.
# a=[1,2,3]
# print(a[4])  #!Index error!!


#my_dict = {'name' : 'Max'}
# print (my_dict['age'])  #! Key Error!!

# ----RAISING EXCEPTIONS!
x = 5
if x < 0:
    raise Exception("X should be positive!!")

y = 5
# *Will throw assertion error if assertion is not true!!
assert(y >= 0), 'Y is not positive!!!'

# ---HANDLE EXPRESSIONS WITH TRY...EXCEPT

try:
    a = 5 / 0
except:
    print('Something Very Terrible Happenned!!')

try:
    a = 5 / 0
except Exception as e:
    print(e)  # *Prints error message


try:
    a = 5 / 0
except ZeroDivisionError:  # *If you know specific type of error
    print('Something Very Terrible Happenned!!')


try:  # *Can try multiple operations.
    a = 5 / 1
    b = a + 4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:  # *Can also have else clause in try except to run if no exception occurs!
    print("Congratulations!! Copacetic!!")
finally:  # *Can also have finally clause in try except. Runs whether there's an exception or not. Mostly used to make cleanup operations
    print('cleaning up...')


# ----DEFINE OUR OWN ERRORS AND EXCEPTIONS
# * Define own error classes by subclassing from the base error classes.

# *It is good to give these classes names with Error at the end
class ValueTooHighError (Exception):
    pass


class ValueTooLowError (Exception):  # *Longer way
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError("Hii ni mingi sana!")
    if x < 50:
        raise ValueTooLowError('ni kidogo sana!! Ongezaa!!', x)


try:
    test_value(20)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.value, e.message)
