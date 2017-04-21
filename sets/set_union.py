# Reading first input, not used anywhere in the program
first_input = input()
# Reading the input->split->parse to int->elements to set
set1 = set(map(int, input().split()))
# Same as second_input
second_input = input()
# Same as set2
set2 = set(map(int, input().split()))
# Union of set1 and set2 returns the set of unique elements there in both set1 and set2
# We can also use set1 | set2 , the or operator.
set3 = set1.union(set2)
# Printing the count of elements in Set
print(len(set3))