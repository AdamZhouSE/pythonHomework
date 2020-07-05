nums = input()
nums = nums[1:-1].split(',')
dp = []

for i in range(len(nums)):
    nums[i] = int(nums[i])

nums.sort()

count = 1
for i in range(1, len(nums)):
    if nums[i] == nums[i - 1] + 1:
        count += 1
    else:
        dp.append(count)
        count = 1

print(max(dp))