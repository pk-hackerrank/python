# if input is 5 then the output should be
#1
#121
#12321
#1234321
#123454321

# All are form of 1^2 , 11^2, 111^2 ....
# and the given condition 0 < N < 10
# Looping through input range
for i in range(1,int(input())+1):
    # x**y is short form of power function
    print((111111111//(10**(9-i)))**2)