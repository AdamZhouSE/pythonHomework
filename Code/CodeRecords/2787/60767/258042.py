def leastSteps(nums):
    n = len(nums)
    nums.sort()
    steps = 0
    for i in range(0,n):
        steps += abs(i+1-nums[i])
    return steps

n = int(input())
temp = input().split(" ")
nums = []
for t in temp:
    nums.append(int(t))
res = leastSteps(nums)
print(leastSteps(nums))