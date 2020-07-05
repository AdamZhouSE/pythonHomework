target = int(input())
nums = list(map(int, input().split(",")))
length = len(nums)
for i in range(len(nums)):
    result = 0
    for j in range(i, len(nums)):
        result += nums[j]
        if result >= target:
            length = min(length, j-i+1)
            break
print(length)
