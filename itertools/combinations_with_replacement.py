# Importing combinations_with_replacement from itertools
from itertools import combinations_with_replacement
# Reading input string and r for combinations_with_replacement or in short calling as cwr 
input_string, r_for_cwr = input().split()
# Sorting the string before applying cwr to get the str in lexicographic order
input_string = ''.join(sorted(input_string))
# Getting cwr for sorted input string and given r
input_string_cwr = list(combinations_with_replacement(input_string, int(r_for_cwr)))
# Looping through the list of tuples
for el in input_string_cwr:
    # Converting tuple to string and printing.
    print(''.join(el))