def check_weird_or_not(n):
    if(n%2 != 0):
        print("Weird")
    else:
        if n>=2 and n<=5:
            print("Not Weird")
        elif n>=6 and n<=20:
            print("Weird")
        else:
            print("Not Weird")

if __name__ == '__main__':
    n = int(input())
    check_weird_or_not(n)
    