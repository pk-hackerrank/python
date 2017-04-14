def swap_case(s):
    result = ""
    for _ in s: # Looping through all characters in String
        if _.isupper(): # Checking whether the character is upper case or not.
            result +=  _.lower() # converting character to lower case.
        else:
            result +=  _.upper() # converting character to upper case.
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s) # Calling the swap_case function
    print(result)