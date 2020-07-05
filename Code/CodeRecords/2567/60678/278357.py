nums = eval(input())
for i in range(0, len(nums)):
    nums[i] = int(nums[i])
lower = int(input())
upper = int(input())

count = 0
for start in range(0, len(nums)):
    sum = 0
    for end in range(start, len(nums)):
        sum += nums[end]
        if lower <= sum and sum <= upper:
            count += 1
print(count)