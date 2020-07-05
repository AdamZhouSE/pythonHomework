nums=input()
def judge(nums):
    if len(nums)==1:
        return True
    for x in range(0,len(nums)-1):
        if nums[x+1]<nums[x]:
            return False
    return True
def judgelength(nums):
    if judge(nums):
        return len(nums)

    for t in range(len(nums),0,-1):
        for x in range(0,len(nums)-t+1):
            if judge(nums[x:x+t]):
                return t
print(judgelength(nums))