nums=list(map(int, input().split(",")))
nums=sorted(nums)
def calulateabs(nums):
    mini=nums[0]
    maxi=nums[-1]
    res=[]
    for x in range(mini,maxi+1):
        count=0
        for t in nums:
            count+=abs(t-x)
        res.append(count)
    return min(t for t in res)
print(calulateabs(nums))