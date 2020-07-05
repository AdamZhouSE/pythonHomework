n=int(input())
a=list(map(int,input().split()))
maxOfB=a[0]
tmp=a[0]
index=0
for i in range(1,n):
    tmp+=a[i]
    if tmp>maxOfB:
        maxOfB=tmp
        index=i
res=maxOfB
for i in range(index+1,n):
    res-=a[i]
print(res)