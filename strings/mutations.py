def mutate_string(string, position, character):
    # As described in the question we can solve it in two ways. 
    # We will comment out one way i.e. using substring.
    str_list = list(string)
    str_list[position] = character
    list_str = "".join(str_list)
    # or the second way
    # list_str = string[:position] + character + string[position+1:]
    return list_str

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)