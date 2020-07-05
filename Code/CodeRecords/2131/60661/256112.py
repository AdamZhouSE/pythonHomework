def isArith(nums):
    space=nums[1]-nums[0]
    for i in range(2,len(nums)):
        if nums[i]-nums[i-1]!=space:
            return False
    return True

nums=list(eval(input()))
res=0
nums.sort()
for i in range(len(nums)-2):
    for j in range(i+2,len(nums)):
        if isArith(nums[i:j+1]):
            res+=1
        else:
            break
print(res)