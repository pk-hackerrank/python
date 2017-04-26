# Importing combinations from itertools
from itertools import combinations
# Getting the input string and counter in a single line
input_string, counter = input().split()
# Sorting the string in lexicographic order
input_string = ''.join(sorted(input_string))
# Converting string to int
counter = int(counter)
# Looping through each combination counter
for i in range(1, counter+1):
    # Getting the combinations list of tuples
    str_combinations = list(combinations(input_string, i))
    # Looping through the list of tuples
    for el in str_combinations:
        # Printing the combined string of tuple.
        print(''.join(el))