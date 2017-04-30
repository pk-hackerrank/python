# Not sure how this code worked, havent understood the problem statement clearly.
from collections import deque
t = int(input())
for j in range(t):
    answer = 'Yes'
    d = deque()
    total = int(input())
    [d.append(int(x)) for x in input().split()]
    biggest = max(d)
    if biggest != d[0] and biggest != d[len(d)-1]:
        answer = 'No'

        
    while len(d) :        
        if biggest < d[0] and biggest < d[len(d)-1]:
            answer = 'No'
            break
        elif d[0] >= d[len(d)-1]:
            biggest = d[0]
            d.popleft()
        else: 
            biggest = d[len(d)-1]
            d.pop()
    print (answer)