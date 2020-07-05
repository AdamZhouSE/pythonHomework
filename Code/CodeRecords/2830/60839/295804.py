import math

lis=input().split(" ")
base=int(lis[0])
k=int(lis[1])

lis=list(map(int,input().split(" ")))

ans=0
if base%2==0:
    print("even" if lis[len(lis)-1]%2==0 else "odd")
else:
    for i in range(k-1,-1,-1):
        ans+=lis[i]
    print("even" if ans%2==0 else "odd")