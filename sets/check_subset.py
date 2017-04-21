for i in range(int(input())):
    a = int(input()); A = set(input().split()) 
    b = int(input()); B = set(input().split())
    # Or we can also use A.issubset(B) function directly
    if A.intersection(B) == A:
        print("True")
    else:
        print("False")