nums=list(map(int, input().split(",")))
def findmax(nums):
    if len(nums)==1:
        return 0
    res = []

    for x in range (0,len(nums)):
        temp=nums[x:]+nums[0:x]
        res.append(temp)
    calculate_result=[]
    for h in res:
        sum=0
        for i in range(0,len(nums)):
            sum+=i*h[i]
            calculate_result.append(sum)
    return max(x for x in calculate_result)
print(findmax(nums))