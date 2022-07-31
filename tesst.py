# ---PERMUTATIONS----
# *Permutations will return all possible orderings of an input
from itertools import permutations

a1 = [1, 2, 3]
perm = permutations(a1)
print(list(perm))  # *Convert to list before printing!! Prints all permutations

perm2 = permutations(a1, 2)  # *Can specify length of permutations!!
print(list(perm2))
