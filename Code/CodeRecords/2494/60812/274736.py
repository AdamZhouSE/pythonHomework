nums = [int(i) for i in input()[1:-1].split(',')]
n = len(nums)
res = 0
for i in range(n-1):
    for j in range(i+1, n):
        if nums[i] > nums[j]*2:
            res += 1
print(res)