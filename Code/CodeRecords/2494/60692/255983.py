nums = input()[1:-1].split(",")
nums = [int(i) for i in nums]
count = 0
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j] * 2:
            count += 1
print(count)