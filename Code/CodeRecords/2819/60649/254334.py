from collections import Counter
n=int(input())
a=list(map(int,input().split()))
count=Counter(a)
k1,k2,k3,k4=count[1],count[2],count[3],count[4]
res=k4+k3+k2//2
k1=k1-k3 if k1>k3 else 0
if k2%2==1:
    res+=1
    k1=k1-2 if k1>2 else 0
res+=k1//4
if k1%4!=0:
    res+=1
print(res)