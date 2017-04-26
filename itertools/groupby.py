# importing groupby from itertools
from itertools import groupby
# taking the input string
given_input = input()
# groupby gives a iterable tuple (k, g) and g is also iterable 
# Forming the list from iterable g and length of list gives the no of
# times the k is consecutive occurences.
groupby_list = [(len(list(g)), int(k)) for k,g in groupby(given_input)]
# Printing the list in string format with space separated.
print(*groupby_list)