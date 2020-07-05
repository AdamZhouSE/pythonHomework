def pancakeSort(nums):
    res = []
    for i in range(len(nums),1,-1):
        index = findMax(nums[:i])
        nums = nums[:index][::-1] + nums[index:]
        nums = nums[:i][::-1]
        if(index>0):
            res.append(index)
        res.append(i)
    return res


def findMax(nums):
    index = 0
    for i in range(1,len(nums)):
        if(nums[i]>=nums[index]):
            index = i
    return index

temp = eval(input())
nums = []
for t in temp:
    nums.append(int(t))
print(pancakeSort(nums))