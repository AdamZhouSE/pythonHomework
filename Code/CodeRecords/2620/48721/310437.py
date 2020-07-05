import math
num=int(input())
res=0
for i in range(num):
    N=int(input())
    for j in range(N+1):
        res=res+pow(j,5)
    print(res)
    res=0