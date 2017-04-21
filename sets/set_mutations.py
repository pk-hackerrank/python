# Take the first input which is not used in the code.
first_input = input()
# The main set where the operations need to be performed.
main_set = set(map(int, input().split()))
# Loop count for no of operations
loop_count = int(input())
# Looping through operations
for i in range(loop_count):
    # Retrieving operation and num of elements, where as num_of_elements is not used anywhere in code.
    operation, num_of_elements = input().split()
    # taking the input of set which is input for operation on main_set
    given_set_for_operation = set(map(int, input().split()))
    # if else chain for operation checks
    if operation == 'intersection_update':
        main_set.intersection_update(given_set_for_operation)
    elif operation == 'update':
        main_set.update(given_set_for_operation)
    elif operation == 'difference_update':
        main_set.difference_update(given_set_for_operation)
    # Only left operation is symmetric_difference_update so no need to do elif here
    else:
        main_set.symmetric_difference_update(given_set_for_operation)

# Printing the sum of all elements in the set.
print(sum(main_set))