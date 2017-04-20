# Take the first input, this is not used anywhere in program
m = int(input()) 
# Split the given input, convert to int using map, get the list from map, get the set from list
set1 = set(list(map(int, input().split()))) 
# Take another input which is not used in program
n = int(input())
# Same as above step, split -> int -> map -> list -> set
set2 = set(list(map(int, input().split())))
# Objective is to find the sorted items which are either in m and n but not in both
# s1 -> # Values which exist in set1 but not in set2
s1 = set1.difference(set2)
# s2 -> # Values which exist in set2 but not in set1
s2 = set2.difference(set1)
# Union the s1 and s2 then convert to list and use sorted() to get sorted order
l = sorted(list(s1.union(s2)))
# looping through sorted list and printing each
for i in l:
    print(i)