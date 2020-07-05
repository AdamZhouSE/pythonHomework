def getLen(nums,mid):
    cnt=0
    tmpsum=0
    for num in nums:
        if tmpsum+num>mid:
            cnt+=1
            tmpsum=num
        else:
            tmpsum+=num
    cnt+=1
    return cnt
def func(nums,m):
    lo=max(nums)
    hi=sum(nums)
    while lo<hi:
        mid=lo+(hi-lo)//2
        length=getLen(nums,mid)
        if length>m: lo=mid+1
        elif length<m: hi=mid-1
        else: hi=mid
    return lo
nums=eval("["+input()+"]")
print(func(nums,int(input())))