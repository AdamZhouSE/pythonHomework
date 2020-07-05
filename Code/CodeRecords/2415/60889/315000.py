def maxaddtree(nums):
    if len(nums) == 0:
        return [1,[]]
    if len(nums) == 1:
        return [nums[0],[nums[0]]]
    if len(nums) == 2:
        return [nums[0]+nums[1],[nums[0],nums[1]]]
    maxnum = 0
    maxtree = 0
    for i in range(len(nums)):
        left = maxaddtree(nums[:i])
        right = maxaddtree(nums[i+1:])
        if left[0]*right[0]+nums[i]>maxnum:
            maxnum = left[0]*right[0]+nums[i]
            a = left[1].copy()
            a.insert(0,nums[i])
            maxtree = a+right[1]
    return [maxnum,maxtree]




length = input()
nums = input().strip(" ").split(" ")
nums = list(map(int,nums))
a = maxaddtree(nums)
print(a[0])
preOrder = []
for i in a[1]:
    for j in range(len(nums)):
        if i == nums[j]:
            preOrder.append(j+1)
for i in preOrder:
    print(i,end=" ")