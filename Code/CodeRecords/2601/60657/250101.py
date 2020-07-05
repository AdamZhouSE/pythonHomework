import math
m=int(input())
n=int(input())
k=int(input())
all=[]
def cal(m,n,k):
    cons=[]
    for i in range(1,m+1):
        for j in range(1,n+1):
            all.append(i*j)
    all.sort()
    return all[k-1]
print(cal(m,n,k))