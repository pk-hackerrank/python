n = input()
# Reading first list
list1 = list(map(int, input().split()))
# Reading second list then to set
set1 = set(list(map(int, input().split())))
set2 = set(list(map(int, input().split())))
count = 0
# Looping through elements in 
for el in list1:
    # checking the element existence Set
    if el in set1:
        count += 1
    elif el in set2:
        count -= 1
print(count)