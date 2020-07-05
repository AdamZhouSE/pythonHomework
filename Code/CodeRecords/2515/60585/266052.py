arr=list(map(int,input().strip().split(',')))
m=eval(input())
n=len(arr)
l=max(arr)
r=sum(arr)
while l<r:
    count=1
    sums=0
    mid=(l+r)//2
    for i in arr:
        sums+=i
        if sums>mid:
            count+=1
            sums=i
    if count<=m:
        r=mid
    else:
        l=mid+1
print(l)