nums=list(map(int,input().strip().split(",")))
m=int(input())
l=max(nums)
r=sum(nums)+1
while l<r:
    mid=l+(r-l)//2
    count=0
    temp=0
    for n in nums:
        count+=n
        if count>mid:
            temp+=1
            count=n
    if count>0:
        temp+=1
    if temp<=m:
        r=mid
    else:
        l=mid+1
print(l)