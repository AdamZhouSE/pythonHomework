tem = input().split(',')
nums = []
for n in tem:
    nums.append(int(n))
nums.sort()
print(nums[0])