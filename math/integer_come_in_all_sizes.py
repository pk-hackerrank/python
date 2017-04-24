# a,b,c,d as 9, 29, 7, 27
# after calculation of a**b + c**d leads to 
# 4710194409608608369201743232 which wont fit in long long int of C++ or a 64-bit integer.
# So python can store any big integer
a,b,c,d = int(input()),int(input()),int(input()),int(input())
print(a**b + c**d)