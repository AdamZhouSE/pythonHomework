outcome = []
nums = eval(input())

nums.sort()

index = 0
target = len(nums) // 3
count = 0
tempCmp = nums[0]
while index < len(nums):
    if nums[index] == tempCmp:
        count += 1
        if count > target:
            outcome.append(tempCmp)
            while index < len(nums) and nums[index] == tempCmp:
                index += 1
        if index >= len(nums):
            break
    if nums[index] != tempCmp:
        tempCmp = nums[index]
        count = 1
    index += 1

print(outcome)