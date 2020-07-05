nums = input()
nums = nums[1: len(nums)-1].split(",")
n = len(nums)
target = int(input())
x = -1
for i in range(n):
    nums[i] = int(nums[i])
for i in range(n):
    if nums[i] == target:
        x = i
        break
print(x)