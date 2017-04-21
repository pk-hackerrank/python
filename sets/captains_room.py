# didnt get the idea of how to solve this problem using Set. So using list and dictionary it can be solved.
# Read all room numbers in list, loop through one by one, maintain a dictionary of room number as key and no
# of times it appeared (count) as value, the captain room will only have the count as 1
# Reading first input which is not used anywhere so its a trash.
trash_input = input()
# Reading input of room numbers in the list
input_list = list(map(int, input().split()))
# Creating empty dictionary
counter_dict = {}
for i in input_list:
    # Getting the counter of room number if not present return 0 as default.
    count = counter_dict.get(i, 0)
    # Incrementing counter by 1
    count+=1
    # Assigning the new counter value
    counter_dict[i] = count
# Looping through elements in dictionary    
for key,value in counter_dict.items():
    # checking the room count apperance to be equal to 1 and breaking the loop
    if value == 1:
        captain_room = key
        break

# Printing captain room.
print(captain_room)