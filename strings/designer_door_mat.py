N, M = map(int,input().split())
# Closely observe output with N, M the sequence we can come up with this logic easily.
for i in range(1,N,2): 
    print(("-"*((M//2)-i-(i//2)))+(".|."*i)+("-"*((M//2)-i-(i//2))))
print("-"*((M-6)//2)+"WELCOME"+"-"*((M-6)//2))
for i in range(N-2,-1,-2): 
    print(("-"*((M//2)-i-(i//2)))+(".|."*i)+("-"*((M//2)-i-(i//2))))