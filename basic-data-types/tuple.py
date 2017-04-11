import builtins # to get hash function
if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    integer_tuple = tuple(integer_list)
    print(hash(integer_tuple)) # hash function is available in buitlins module