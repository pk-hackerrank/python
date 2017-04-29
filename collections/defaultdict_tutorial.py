# Importing defaultdict from collections
from collections import defaultdict
# Creating defaultdict with value field as list type
default_dict_list = defaultdict(list)
# Reading n_counter and m_counter
n_counter, m_counter = map(int, input().split())
# Looping through counters
for i in range(1,n_counter+1):
    # Reading input char
    n_input_char = input()
    # Appending counter as index the list with char key
    default_dict_list[n_input_char].append(i)
# Looping through m_counter
for _ in range(m_counter):
    # Reading input char
    m_input_char = input()
    # Checking if list is empty or not
    if not default_dict_list[m_input_char]:
        # Printing -1 if the list is empty
        print(-1)
    # Else printing indices of particular char
    else:
        print(*default_dict_list[m_input_char]) 