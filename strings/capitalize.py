def capitalize(string):
    list = string.split(' ')
    for i in range(0, len(list)):
        list[i] = list[i].capitalize()
    string = " ".join(list)
    # Another short form
    # string = " ".join([x.capitalize() for x in string.split(' ')]) # Learn more about list compressions
    return string
if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)