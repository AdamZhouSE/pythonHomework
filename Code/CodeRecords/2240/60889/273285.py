def findEqual(nums,nowNum,target):
    if len(nums)==0:
        if nowNum==target:
            return True
        else:
            return False
    newNums = nums.copy()
    newNowNum = newNums.pop(0)+nowNum
    if findEqual(newNums.copy(),nowNum,target):
        return True
    else:
        return findEqual(newNums.copy(),newNowNum,target)

nums = input().split(",")
nums = list(map(int,nums))
summary = 0
for i in nums:
    summary = summary + i
print(findEqual(nums,0,summary/2))