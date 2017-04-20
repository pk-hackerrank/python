# Reading just for name sake.
n = int(input())
# Directly reading elements to set
s = set(map(int, input().split()))
# Getting number of instructions 
no_of_instructions = int(input())
# Looping through instructions
for i in range(no_of_instructions):
    # Directly not splitting input() into two elements since if input is 'pop' it may raise an Error
    op_n_el = input()
    # Checking the instruction is pop
    if op_n_el.startswith('pop'):
        s.pop()
    else:
        op, el = op_n_el.split()
        if(op == 'discard'):
            s.discard(int(el))
        else:
            s.remove(int(el))
# Calling sum function directly on set s.
print(sum(s))