# Import OrderedDict from collections
from collections import OrderedDict
# Taking in no of words as input
no_of_words = int(input())
# Initializing empty OrderedDict
words_dict = OrderedDict()
# Looping through counter
for _ in range(no_of_words):
    # Reading input word
    word = input()
    # We can also use try and except to initialize the value
    # Incrementing the counter word
    words_dict[word] = words_dict.get(word, 0) + 1 
# We can also use len(words_dict) will return the same
# Printing size of dictionary
print(len(words_dict.keys()))
# We can also print using 
# print(*words_dict.values())
# Looping through values and printing with space separated.
for val in words_dict.values():
    print(val, end=" ")