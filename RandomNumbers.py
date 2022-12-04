
# # Generate psudo-random numbers which can be reproduced. Not cryptographically secure.
# import random

# a = random.random()  # Prints random float between 0 and 1 (0 <= a < 1)
# print(a)
# # Prints random float between 1 and 10 (including 1 and 10)
# b = random.uniform(1, 10)
# print(b)
# # Prints random integer between 1 and 10 (inclusive of upper bound)
# c = random.randint(1, 10)
# print(c)
# # Prints random integer between 1 and 10 (exclusive of upper bound)
# d = random.randrange(1, 10)
# print(d)
# e = random.choice([1, 2, 3, 4, 5])  # Prints random element from list
# print(e)
# # Prints random sample of 3 elements from list
# f = random.sample([1, 2, 3, 4, 5], 3)
# print(f)
# # Prints random number from normal distribution with mean 0 and standard deviation 1
# g = random.normalvariate(0, 1)
# print(g)

# mylist = list("ABCDEFGH")
# h = random.choice(mylist)  # Prints random element from list
# print(h)
# #! Ranom.choices Will not work! Replaced with random.sample
# j = random.sample(mylist, 3)  # Prints random sample of 3 elements from list
# print(j)

# # Shuffle a list in place!!
# random.shuffle(mylist)
# print(mylist)

# # Set seed to reproduce results
# # *seed(1) will always produce the same results
# random.seed(1)
# print(random.random())
# print(random.randint(1, 10))

# # *seed(2) will always produce the same results
# random.seed(1)
# print(random.random())
# print(random.randint(1, 10))


# * Secrets Module
# * This module is used to generate cryptographically secure random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.
# * The secrets module should be used in preference to the default pseudo-random number generator in the random module, which is designed for modelling and simulation, not security or cryptography.
# * The secrets module provides access to the most secure source of randomness that your operating system provides.
# * The secrets module is not available on Python 3.5 or older.

import secrets

# Generate a random integer between 1 and 10 (inclusive of upper bound)
a = secrets.randbelow(10) + 1
print(a)

b = secrets.randbits(4)  # Generate a 4-bit random integer (0 <= b < 16)
print(b)

mylist = list("ABCDEFGH")
c = secrets.choice(mylist)  # Prints random element from list
print(c)


# *  Numpy Module
# *  Numpy is a Python library used for working with arrays.
# * Numpy seed is preferred

# import numpy as np

# # Create an array containing 6 random integers between 1 and 10 (inclusive of upper bound)
# a = np.random.rand(6) * 10 + 1 # Prints random float between 1 and 10 (including 1 and 10)
# print(a)

# # Create an array containing 6 random integers between 1 and 10 (exclusive of upper bound)
# b = np.random.randint(1, 10, (3,4))
# print(b)

# arr = np.array([1, 2, 3, 4, 5])
