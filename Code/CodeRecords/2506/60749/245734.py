nums=input()

def longest(nums):
    if len(nums)==1:
        return 1
    max=0
    for x in range(0, len(nums)):
        res = [nums[x]]
        for t in range(x+1,len(nums)):
            if nums[t]>res[-1]:
                res.append(nums[t])
        if len(res)>max:
            max=len(res)
    return max
print(longest(nums))
    
