# Importing deque from collections
from collections import deque
# Taking input counter
counter = int(input())
# Initializing deque list
deque_list = deque()
# Looping through counter to take input of next lines.
for _ in range(counter):
    # Stripping the input to remove extra spaces at the end.
    given_input = input().strip()
    # Comparint the given input operation and performing the same.
    if given_input == 'pop':
        deque_list.pop()
    elif given_input == 'popleft':
        deque_list.popleft()
    else:
        # Command needed and item needed to perfrom operation.
        command, item = given_input.split()
        if command == 'append':
            deque_list.append(item)
        elif command == 'appendleft':
            deque_list.appendleft(item)
# Printing the list with space separated.
print(*deque_list)