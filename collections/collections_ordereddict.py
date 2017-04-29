# Import OrderedDict from collections
from collections import OrderedDict
# Taking input of no of orders
no_of_orders = int(input())
# Initializing empty OrderedDict
orders_in_orderddict = OrderedDict()
# Looping through 
for _ in range(no_of_orders):
    input_list = input().split()
    # Getting the prize from the input
    prize = int(input_list[-1])
    # Getting the item name by removing the last element i.e. prize
    item_name = " ".join(input_list[:-1])
    # Calculating prize, get the default prize as 0 if element does not exists
    # or get the value and adding to the prize
    orders_in_orderddict[item_name] = orders_in_orderddict.get(item_name, 0) + prize
# Looping through the keys of OrderedDict    
for key in orders_in_orderddict.keys():
    # Print key and value of OrderedDict.
    print(key, orders_in_orderddict[key])