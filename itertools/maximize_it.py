# Importing product from the itertools
from itertools import product
# Reading loop_count and divisor directly as int using map and input().split()
loop_count, divisor = map(int,input().split())
# Initializing square_vals_list empty
square_vals_list = []
# Looping through counter
for _ in range(loop_count):
    # Reading elements into list and taking from 1 to n-1 or removing 1 element
    elements_list = list(map(int,input().split()))[1:]
    # Preparing list of elements of squares for each element.
    elements_list = [x*x for x in elements_list]
    # Appending elements to square_vals_list
    square_vals_list.append(elements_list)
# Calculating the cartesian product list
cartesian_product_list = list(product(*square_vals_list))
# calculating sum of tuple by divisor for each element(tuple) in cartesian product list
after_division_list = [sum(tuple_el)%divisor for tuple_el in cartesian_product_list]
# Getting the max of after_division_list will give the required result.
print(max(after_division_list))