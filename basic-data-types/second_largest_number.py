# Finding the second largest number in a list.
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split())) # Converting input string into list by map and list()
    new = [x for x in arr if x != max(arr)] # Using list compressions building new list removing the highest number
    print(max(new)) # Since we removed the max number in list, now the max will give the second largest from original list.