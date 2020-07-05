tem = input().split(',')
nums = []
for n in tem:
    nums.append(int(n))
minnum = min(nums)
for n in range(len(nums)):
    nums[n] = nums[n] - minnum
print(sum(nums))