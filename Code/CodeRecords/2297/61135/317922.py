import math
N=int(input())
num=input().split(" ")
K=int(input())
b=2**(K-1)
e=2**K
res=[]
if(b<N):
    for i in range(b-1,e-1):
        if(i<=len(num)-1):
            res.append(num[i])
        else:
            break
    print(" ".join(res))
else:
    print("EMPTY")