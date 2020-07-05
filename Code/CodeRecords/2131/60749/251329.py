nums=list(map(int, input().split(",")))
def judgenumarray(nums):
    c=nums[1]-nums[0]
    for x in range(1, len(nums)):
        if not nums[x]-nums[x-1]==c:
            return False
    return True
def count(nums):
    count=0
    if len(nums)<=2:
        return 0
    if judgenumarray(nums):
        count+=1
    for x in range(3,len(nums)):
        for t in range(0,len(nums)-x+1):
            if judgenumarray(nums[t:t+x]):
                count+=1
    return count
print(count(nums))  