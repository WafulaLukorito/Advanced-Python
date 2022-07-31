
from collections import deque


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
