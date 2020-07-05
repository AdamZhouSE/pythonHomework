nums = [int(x) for x in input().split(',')]
target = int(input())
index = -1
for i in range(0, len(nums)):
    if nums[i] == target:
        index = i
        break
print(index)
