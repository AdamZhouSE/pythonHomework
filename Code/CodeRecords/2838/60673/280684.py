inp = int(input())
nums = input().split(" ")
for i in range(inp):
    nums[i] = int(nums[i])
nums.sort()
sums = 0
for i in range(int(inp / 2)):
    sums += int(pow((nums[i] + nums[inp-1-i]), 2))
print(sums)