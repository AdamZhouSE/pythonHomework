
nums =input().split(',')
n = len(nums)

for i in range(0 ,n):
    nums[i ] =int(nums[i])


result =0
C =0
for i in range(0, n - 2):
    for j in range(i + 1, n - 1):
        for m in range(j + 1, n):
            x1 = nums[i]
            x2 = nums[j]
            x3 = nums[m]
            
            if ((x1 + x2 > x3) and (x1 + x3 > x2) and (x2 + x3 > x1)):
                C = x1 + x2 + x3
            result = max(result, C)

print(result)