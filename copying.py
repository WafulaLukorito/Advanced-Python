
#* SHALLOW VS DEEP COPY

#? Shallow copy: one level deep, creates a new object but does not create copies of nested objects. Changes to mutable nested objects will affect the original object.
#? Deep copy: creates a new object and recursively copies all nested objects. Changes to any nested objects will not affect the original object.

#? Assignment creates a reference to the original object, not a copy. Changes to the new variable will affect the original variable.
original_list = [1, 2, 3]
assigned_list = original_list  # This does not create a new list, it just creates a new reference to the same list
assigned_list.append(4)
print(original_list)  # Output: [1, 2, 3, 4] (original_list is modified because assigned_list is just a reference to the same list)

orig = 5
cpy = orig
cpy = 6
print (cpy) # Output: 6 (cpy is modified, but orig is not affected because integers are immutable)
print (orig) # Output: 5 (orig is unchanged)


#? Shallow copy creates a new object, but the contents of the object are still references to the original objects. Changes to mutable objects within the new object will affect the original objects.
import copy
original_list = [1, [2, 3], 4]
#shallow_copy = copy.copy(original_list)  # Shallow copy
#or
#shallow_copy = original_list[:]  # Shallow copy using slicing
#or

#shallow_copy = list(original_list)  # Shallow copy using list() constructor

#or 

shallow_copy = original_list.copy()  # Shallow copy using copy() method

shallow_copy[1].append(5)
print(original_list)  # Output: [1, [2, 3, 5], 4] (the inner list is modified because it's a reference to the same list)


original_dict = {'a': 1, 'b': [2, 3]}
#shallow_copy_dict = copy.copy(original_dict)  # Shallow copy of a dictionary
#or
#shallow_copy_dict = original_dict.copy()  # Shallow copy of a dictionary using copy() method
shallow_copy_dict = dict(original_dict)  # Shallow copy of a dictionary using dict() constructor
shallow_copy_dict['b'].append(4)
print(original_dict)  # Output: {'a': 1, 'b': [2, 3, 4]} (the list associated with key 'b' is modified because it's a reference to the same list)

orig = 5
cpy = orig
cpy = 6
print (cpy) # Output: 6 (cpy is modified, but orig is not affected because integers are immutable)
print (orig) # Output: 5 (orig is unchanged)

#? Deep copy creates a new object and recursively copies all objects within it. Changes to any objects within the new object will not affect the original objects.
import copy
original_list = [1, [2, 3], 4]
# my_shallow_copy = copy.copy(original_list)  # Shallow copy
deep_copy = copy.deepcopy(original_list)  # Deep copy
deep_copy[1].append(5)

print(original_list)  # Output: [1, [2, 3], 4] (the inner list is not modified because it's a completely separate copy)

#?Custom objects and copying
# When you create a shallow copy of a custom object, the new object will have the same attributes as the original object, but if any of those attributes are mutable objects (like lists or dictionaries), they will still reference the same objects in memory. Therefore, changes to those mutable attributes in the copied object will affect the original object. In contrast, when you create a deep copy of a custom object, all attributes and nested objects are recursively copied, so changes to any attribute in the copied object will not affect the original object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Kamau", 30)
person2 = copy.copy(person1)  # Shallow copy of person1
person3 = copy.deepcopy(person1)  # Deep copy of person1

person2.name = "Wamboi"  # Modifying the name attribute of person2
print(person1.name)  # Output: Kamau (person1's name is unchanged because it's a shallow copy, but the name attribute is a string which is immutable, so it creates a new string object for person2)
print(person2.name)  # Output: Wamboi (person2's name is modified)

class Company:
    def __init__(self, boss, employees):
        self.boss = boss
        self.employees = employees

company = Company("TechCorp", ["Alice", "Bob"])
company_clone = copy.copy(company)  # Shallow copy of company

company_clone.boss.age = 40  # Modifying the age attribute of the boss in the cloned company
print(company.boss.age)  # Output: 40 (the boss's age is modified in the original company because it's a shallow copy and the boss is a mutable object)

company_clone_deep = copy.deepcopy(company)  # Deep copy of company
company_clone_deep.boss.age = 50  # Modifying the age attribute of the boss in the deep cloned company
print(company.boss.age)  # Output: 40 (the boss's age in the original company is unchanged because it's a deep copy and the boss is a completely separate object)