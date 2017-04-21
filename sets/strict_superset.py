# Reading the main set
main_set = set(map(int, input().split()))
# Reading loop count
loop_count = int(input())
# setting flag for strict superset
is_strict_superset = True
# Looping through counter
for i in range(loop_count):
    # Reading the input set
    superset_check_set = set(map(int,input().split()))
    # as per the problem if atleast 1 set is not strict super set we can return false
    # So not with and condition applies right here.
    if(not(main_set.issuperset(superset_check_set) and (len(main_set) != len(superset_check_set)))):
       is_strict_superset = False
       break
# Printing the flag set value.
print(is_strict_superset)