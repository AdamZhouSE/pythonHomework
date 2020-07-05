def isArithmeticSeries(nums):
    if 2*nums[1] == nums[0]+nums[2]:
        return True
    else:
        return False
    
lenOfSeries = []
nums = list(map(int,input().split(",")))
if len(nums)<3:
    print(0)
else:
    newNums = []
    newNums.append(0)
    a = nums.pop(0)
    newNums.append(a)
    a = nums.pop(0)
    newNums.append(a)
    length = 0
    while len(nums)!=0:
        del newNums[0]
        a = nums.pop(0)
        newNums.append(a)
        if isArithmeticSeries(newNums):
            length = length + 1
        else:
            if length != 0:
                lenOfSeries.append(length)
                length = 0
    if length != 0:
        lenOfSeries.append(length)
    numOfSeries = 0
    for i in lenOfSeries:
        numOfSeries = numOfSeries + i*(i+1)
    print(int(numOfSeries/2))