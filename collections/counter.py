# Importing Counter from collections.
from collections import Counter
# Unused input
_trash = input()
# Reading list of sizes of shoes
input_list = list(map(int, input().split()))
# Calculating the counter dictionary on given shoe size list
counter_dict = Counter(input_list)
# Taking input of loop_counter
loop_counter = int(input())
# Initializing total money earned to 0
total_money = 0
# Looping through 
for _ in range(loop_counter):
    # Taking input as size and money
    size, money = map(int,input().split())
    # Conditional check the dictionary counter value for size is not 0
    # then add money to total money
    # decrement the counter value for size by 1
    if(counter_dict[size] != 0):
        total_money += money
        counter_dict[size] -= 1
# Printing total money earned.
print(total_money)