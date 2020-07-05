import math
tem = input().split(',')
nums = []
for n in tem:
    nums.append(int(n))
avg = math.round(sum(nums)/len(nums))
result = 0
for n in nums:
    x = n - avg
    if x < 0:
        x = -x
    result = result + x
print(result)