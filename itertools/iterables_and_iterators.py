# Importing combinations from itertools
from itertools import combinations
# trash input not used in the code anywhere
trash_int = input()
# Taking input string split and get the list
input_list = input().split()
# Indices count
indices = int(input())
# first way 
# Get the combinations, convert to list
combination_list = list(combinations(input_list, indices))
# initialize counter to 0
count = 0
# Loop through the combination_list
for el in combination_list:
    # check if tuple contains 'a' 
    if 'a' in el:
        count+=1
probability = count/len(combination_list)

# Another way as in editorial may be the best way
#combination_list_total = 0
# we can loop through combinations output since it is a iterable
#for el in combinations(input_list, indices):  
#    combination_list_total += 1
#    count += 'a' in el # increment counter directly with condition
#probability = count/combination_list_total

print(probability)