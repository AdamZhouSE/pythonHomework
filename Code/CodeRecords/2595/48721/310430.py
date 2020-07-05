import math
T=int(input())

for i in range(T):
    s=input().split()
    N=int(s[0])
    K=int(s[1])
    res=pow(K,N-1)
    print(res)