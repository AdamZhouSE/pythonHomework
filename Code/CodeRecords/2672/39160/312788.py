# import math
ref = (1 << 32)-1

t = int(input())

for i in range(t):
    n = int(input().strip())
    n ^= ref
    print(n)