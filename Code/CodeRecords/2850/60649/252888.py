n=int(input())
a=list(map(int,input().split()))
max0=0
tmp=0
for i in range(n):
    if tmp<0:
        tmp=0
    if a[i]==0:
        tmp+=1
        max0=max(max0,tmp)
    else:
        tmp-=1
print(max0+a.count(1))