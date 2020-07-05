def findDuplicate( nums):
    for item in nums:
        if nums.count(item) != 1:
            return item
nums=list(map(int,input().split(',')))
print(findDuplicate(nums))