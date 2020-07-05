#09
nums = eval(input())
n = len(nums)

res = 0
for i in range(0,n-1):
    for j in range(i+1,n):
        if nums[i] > 2*nums[j]:
            res += 1

print(res)