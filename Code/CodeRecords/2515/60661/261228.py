nums=eval(input())
m=eval(input())
l,r=max(nums),sum(nums)
while l<r:
    mid=l+(r-l)//2
    i,count,temp=0,1,0
    while(i<len(nums)):
        temp+=nums[i]
        if temp>mid:
            temp=nums[i]
            count+=1
        i+=1
    #if count==m:
    #    print(mid)
    #    exit()
    if count<=m:
        r=mid
    else:
        l=mid+1
print(l)