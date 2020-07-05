def findEqual(nums,nowNum,target):
    if len(nums)==0:
        if nowNum!=0 and nowNum%target == 0:
            return True
        else:
            return False
    if nowNum != 0 and nowNum%target == 0:
        return True
    newNums = nums.copy()
    newNowNum = newNums.pop(0)+nowNum
    if findEqual(newNums.copy(),nowNum,target):
        return True
    else:
        return findEqual(newNums.copy(),newNowNum,target)

nums = input().split(",")
nums = list(map(int,nums))
target = int(input())
print(findEqual(nums,0,target))