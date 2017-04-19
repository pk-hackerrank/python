import textwrap
from collections import OrderedDict
def merge_the_tools(string, k):
    # your code goes here
    str_list = textwrap.wrap(string, k) # textwrap with wrap method divides the string into k parts.
    final_list = []
    for s in str_list:
        final_list.append(''.join(OrderedDict.fromkeys(s).keys())) # OrderedDict maintains the order.
    for s in final_list:
        print(s)