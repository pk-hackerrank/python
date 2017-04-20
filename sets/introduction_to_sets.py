def average(array):
    array_in_set = set(array)
    sum_of_els = 0
    for a in array_in_set:
        sum_of_els += a
    return sum_of_els/len(array_in_set)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)   
