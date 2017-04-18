def print_rangoli(size):
    alphabets = list('abcdefghijklmnopqrstuvwxyz')
    size_count = 1
    loop_count = 2*size - 1
    alphabets_size = len(alphabets)
    # Print the upper code including the middle 
    for i in range(loop_count,0,-2):
        str = "-"*(i-1)
        sub_list = alphabets[size-size_count:size] # We can concat the two lists and use "-".join
        first_list = list(reversed(sub_list))
        str = str + "-".join(first_list)
        if i != loop_count: # if we concat the lists, this additional check is not required.
            str = str + "-"
        str = str + "-".join(sub_list[1:])
        size_count += 1
        str = str + "-"*(i-1)
        print(str)
    size_count = 1
    # Printing the below cone.
    for i in range(1,loop_count,2):
        str = "-"*(i+1)
        sub_list = alphabets[size_count:size] 
        new_list = list(reversed(sub_list))
        str = str + "-".join(new_list)
        if i != loop_count-2:
            str = str + "-"
        str = str + "-".join(sub_list[1:])
        size_count += 1
        str = str+ "-"*(i+1)
        print(str)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)