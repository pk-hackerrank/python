# Importing permutations from itertools.
from itertools import permutations
# Taking the input split by space into two variables.
string, count = input().split()
# As per requirement the given input is all capital letters and the permutations
# need to be in lexicographic order. Since all capital letters we can directly use
# sorted(str) and join to form string
string = ''.join(sorted(string))
# Calling permutations to get the list of permutations, returns list of tuples
permutation_list = list(permutations(string, int(count)))
# Looping through all elements(tuples) 
for element in permutation_list:
    print(''.join(element)) # forming string from a tuple of characters