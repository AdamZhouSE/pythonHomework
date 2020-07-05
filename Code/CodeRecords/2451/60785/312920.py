def searchInsert( nums, target):
    if target in nums:
        return nums.index(target)
    nums.append(target)
    for i in range(len(nums) - 1):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums.index(target)
nums=list(map(int,input().split(',')))
target=int(input())
print(searchInsert(nums,target))