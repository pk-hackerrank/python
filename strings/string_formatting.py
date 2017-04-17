def print_formatted(number):
    # Getting the width to be separated between Strings
    length = len(bin(number))-1
    # print('{: >{}}'.format("ss"), 3) # prints below
    #    ss
    for i in range(1,number+1):
        print('{: >{}}'.format(str(i),length-1) + '{: >{}}'.format(oct(i)[2:], length) + '{: >{}}'.format((hex(i)[2:]).upper(), length)+ '{: >{}}'.format(bin(i)[2:], length))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)