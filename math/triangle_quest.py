# if input is 5 then the output should be
#1
#22
#333
#4444
#55555

# All are form of 1*1 , 11*2, 111*3 ....
# Loop through the given input divide 111111111 by 10 power of (9 - i) then product the final result with i.
# and the given condition 1 <= N <= 9
# Looping through input range
for i in range(1,int(input())):
    print((111111111//(10**(9-i)))*i)