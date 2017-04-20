loop_num = int(input())
# intializing a empty set
final_set = set([])
for i in range(loop_num):
    el = input()
    # Add element to the Set
    final_set.add(el)
print(len(final_set))