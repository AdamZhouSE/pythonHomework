import math

N=int(input())
for i in range(N):
    s=input().split()
    n=int(s[0])
    k=int(s[1])
    print(int(math.pow(k,n-1)))