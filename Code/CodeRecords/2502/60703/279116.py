n = int(input())
nums = []
res = 0
for i in range(n):
    nums.append((int(input())))
nums.sort()
print(sum(nums[1:]))