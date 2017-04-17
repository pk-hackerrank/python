if __name__ == '__main__':
    w = input()
    # Setting all flags to False.
    p = False;
    q = False;
    r = False;
    s = False;
    t = False;
    # Looping through all the characters from the given input.
    for i in w:
        if not(p) and i.isalnum(): # Checking if character alpha numeric or not.
            p = True;
        if not(q) and i.isalpha(): # checking if character is alphabet or not
            q = True;
        if not(r) and i.isdigit(): # checking if character is number or not
            r = True;
        if not(s) and i.islower(): 
            s = True;
        if not(t) and i.isupper():
            t = True;
    # Printing the changed flags.
    print(p)
    print(q)
    print(r)
    print(s)
    print(t)