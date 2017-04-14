def split_and_join(line):
    split_list = line.split(" ") # String split will split the string into List.
    join_str = "-".join(split_list) # Joins the list with the given string and returns a single string.
    return join_str

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)