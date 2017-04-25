# Importing product from itertools
from itertools import product
# Reading two input lists
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# Finding the cartesian product
C = list(product(A, B))
# Printing the List elements with space separated 
print(*C)